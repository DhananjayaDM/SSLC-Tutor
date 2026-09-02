import os
import time
from difflib import SequenceMatcher
from dotenv import load_dotenv
from groq import Groq
from groq import APIStatusError

from services.retriever import retrieve_all

import json
load_dotenv()
os.makedirs(
    "database",
    exist_ok=True
)

MEMORY_FILE = os.path.join(
    "database",
    "memory.json"
)
def normalize_question(text):

    text = text.lower()

    ignore_words = {
        "what",
        "is",
        "are",
        "the",
        "a",
        "an",
        "explain",
        "define",
        "describe",
        "compare",
        "differentiate",
        "tell",
        "give"
    }

    words = []

    for word in text.split():

        word = word.strip(
            ".,?!:;()[]{}\"'"
        )

        if (
            word
            and word not in ignore_words
        ):
            words.append(word)

    return " ".join(words)


def load_memory():

    if not os.path.exists(
        MEMORY_FILE
    ):
        return []

    try:

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except Exception:

        return []

from difflib import SequenceMatcher


def find_memory(question):

    normalized = normalize_question(
        question
    )

    memories = load_memory()

    best_match = None
    best_score = 0

    for item in memories:

        stored_question = normalize_question(
            item.get(
                "question",
                ""
            )
        )

        score = SequenceMatcher(
            None,
            normalized,
            stored_question
        ).ratio()

        if score > best_score:

            best_score = score
            best_match = item

    print(
        f"\nMemory Match Score: "
        f"{best_score:.2f}"
    )

    if best_score >= 0.85:
        return best_match

    return None

def save_memory(
    question,
    answer,
    topic,
    chapter
):

    normalized = (
        question
        .lower()
        .strip()
    )

    memories = load_memory()

    for item in memories:

        if (
            item.get(
                "question",
                ""
            )
            ==
            normalized
        ):
            return False

    memories.append(
        {
            "question": normalized,
            "answer": answer,
            "topic": topic,
            "chapter": chapter
        }
    )

    with open(
        MEMORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            memories,
            f,
            indent=4,
            ensure_ascii=False
        )

    return True
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_text(doc):

    return doc.get(
        "content",
        doc.get(
            "notes",
            ""
        )
    )


def get_title(doc):

    return doc.get(
        "title",
        doc.get(
            "topic",
            "Unknown Topic"
        )
    )


def expand_query(question):

    query = question.lower()

    replacements = {
        "alu": "alu arithmetic logic unit alu",
        "cu": "cu control unit cu",
        "pc": "pc program counter pc",
        "ir": "ir instruction register ir",
        "mar": "mar memory address register mar",
        "mdr": "mdr memory data register mdr",
        "dma": "dma direct memory access dma",
        "ram": "ram random access memory rma",
        "rom": "rom read only memory rom",
        "cache": "cache memory"
    }

    for short, full in replacements.items():

        query = query.replace(
            short,
            full
        )

    return query

def process_question(question: str):

    #
    # 1. MEMORY LOOKUP
    #
    cached = find_memory(question)

    if cached:
        return {
            "source": "memory",
            "answer": cached["answer"],
            "topic": cached.get(
                "topic",
                "Unknown"
            ),
            "chapter": cached.get(
                "chapter",
                "Unknown"
            )
        }

    #
    # 2. QUERY EXPANSION
    #
    query = expand_query(question)

    #
    # 3. RETRIEVE DOCUMENTS
    #
    docs = retrieve_all(
        query=query,
        k=10
    )

    notes_found = False
    best_doc = {}

    if docs:

        best_doc = docs[0]

        notes_found = (
            best_doc.get(
                "distance",
                999
            ) <= 1.5
        )

    #
    # 4. BUILD CONTEXT
    #
    context_parts = []

    if notes_found:

        for doc in docs[:5]:

            topic = get_title(doc)

            notes = get_text(doc)

            chapter = doc.get(
                "chapter",
                "Unknown"
            )

            context_parts.append(
                f"""
CHAPTER:
{chapter}

TOPIC:
{topic}

NOTES:
{notes}
"""
            )

    context = "\n\n".join(
        context_parts
    )[:5000]

    #
    # 5. PROMPT
    #
    prompt = f"""
You are a Computer Science Exam Preparation Assistant.

QUESTION:

{question}

AVAILABLE NOTES:

{context}

RULES:

1. Use notes as the primary source whenever relevant.

2. If the answer exists in the notes:
   - Answer mainly from the notes.
   - Include important exam points.

3. If the answer is NOT present in the notes:
   - Start the answer with:

     This topic is not present in the provided notes.

   - Then answer using standard academic computer science knowledge.

4. If the notes partially contain the answer:
   - Use notes first.
   - Then enrich the answer with academic knowledge.

5. Use bullet points where appropriate.

6. For algorithms:
   - Mention strategy.
   - Mention complexity.
   - Mention applications.

7. Keep answers exam-oriented.

NOTES_FOUND = {"YES" if notes_found else "NO"}
"""
    #
    # 6. GROQ CALL
    #
    try:

        response = (
            client.chat.completions.create(
                model="openai/gpt-oss-120b",
                temperature=0,
                max_tokens=800,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        answer = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        return {
            "source":
                "notes"
                if notes_found
                else "general",

            "answer": answer,

            "topic":
                get_title(best_doc)
                if notes_found
                else "General Knowledge",

            "chapter":
                best_doc.get(
                    "chapter",
                    ""
                )
                if notes_found
                else ""
        }

    except APIStatusError as e:

        if e.status_code == 429:
            return {
                "source": "error",
                "answer":
                "Rate limit reached. Please try again in a few seconds."
            }

        elif e.status_code == 413:
            return {
                "source": "error",
                "answer":
                "Request too large. Reduce context size."
            }

        else:
            return {
                "source": "error",
                "answer": f"API Error: {e}"
            }

    except Exception as e:

        return {
            "source": "error",
            "answer":
            f"Unexpected Error: {e}"
        }