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


print(
    "\n==================================="
)
print(
    "COMPUTER SCIENCE EXAM ASSISTANT"
)
print(
    "Type 'exit' to quit"
)
print(
    "==================================="
)


while True:

    question = input(
        "\nAsk Question: "
    ).strip()
    if question.lower() in [
        "exit",
        "quit"]:
        print("\nGoodbye!")
        break


    cached = find_memory(
    question
    )

    if cached:
        print(
        f"\nAnswer (Memory Cache)"
        f" [{cached.get('topic', 'Unknown')}]:\n"
        )

        print(
        cached["answer"]
        )

        continue

    try:

        query = expand_query(
            question
        )

        docs = retrieve_all(
            query=query,
            k=10
        )

        if not docs:

            print(
                "\nInformation not found in the provided notes."
            )

            continue

        print(
            "\nRetrieved Topics:\n"
        )

        for doc in docs[:5]:

            print(
                f"- [{doc.get('chapter', 'Unknown')}] "
                f"{get_title(doc)} "
                f"(score={doc.get('score', 0):.3f}, "
                f"distance={doc.get('distance', 0):.3f})"
            )

        best_doc = docs[0]

        print(
            f"\nBest Match: "
            f"{get_title(best_doc)}"
        )

        #
        # Reject unrelated queries
        #

        if best_doc.get(
            "distance",
            999
        ) > 1.5:

            print(
                "\nInformation not found in the provided notes."
            )

            continue

        #
        # Build context using Top 5 Notes
        #

        context_parts = []

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

        prompt = f"""
You are an exam preparation assistant.

STUDY NOTES:

{context}

QUESTION:

{question}

RULES:

1. Use the notes as the PRIMARY source.

2. Answer primarily from the notes.

3. If multiple notes discuss the same topic,
   combine their information.

4. Prefer detailed explanations over brief mentions.

5. You may:
   - simplify explanations
   - provide examples
   - provide worked examples
   - provide truth tables
   - provide exam tips

6. Do not contradict the notes.

7. If information is partially available,
   complete it using standard academic
   computer science knowledge.

8. If information is completely absent,
   say exactly:

   Information not found in the provided notes.

9. Use bullet points whenever useful.

10. Keep answers concise and useful for exams.

11. For binary arithmetic,
    show the complete calculation.

12. For truth tables,
    generate the complete truth table.

13. Maximum 150 words.
"""

        response = (
            client.chat.completions.create(
                model="openai/gpt-oss-120b",
                temperature=0,
                max_tokens=300,
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

        print("\nAnswer:\n")
        print(answer)
        choice = input(
        "\nSave answer to memory? (y/n): "
        ).strip().lower()
        if choice == "y":
            saved = save_memory(
            question=question,
            answer=answer,
            topic=get_title(best_doc),
            chapter=best_doc.get(
            "chapter",
            ""
            )
            )

            if saved:
                print(
            "\nSaved to memory."
            )
            else:
                print(
            "\nQuestion already exists in memory."
            ) 
    except APIStatusError as e:

        if e.status_code == 429:

            print(
                "\nRate limit reached. Waiting 6 seconds..."
            )

            time.sleep(6)

            continue

        elif e.status_code == 413:

            print(
                "\nRequest too large. Reduce context size."
            )

            continue

        else:

            print(
                f"\nAPI Error: {e}"
            )

    except KeyboardInterrupt:

        print(
            "\n\nStopped by user."
        )

        break

    except Exception as e:

        print(
            f"\nUnexpected Error: {e}"
        )