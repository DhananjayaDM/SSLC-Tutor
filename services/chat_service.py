import os
import json
from difflib import SequenceMatcher

from dotenv import load_dotenv
from groq import Groq
from groq import APIStatusError

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
        f"Memory Match Score: "
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
            == normalized
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
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)


def process_question(
    question: str
):

    #
    # MEMORY LOOKUP
    #
    cached = find_memory(
        question
    )

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
    # PROMPT
    #
    prompt = f"""
You are a Computer Science Exam Preparation Assistant.

QUESTION:
{question}

RULES:

1. Answer using standard academic computer science knowledge.

2. Keep answers exam-oriented.

3. Use bullet points whenever appropriate.

4. For theory questions:
   - Give definition
   - Explain concept
   - Mention advantages and disadvantages if applicable

5. For algorithms:
   - Explain the strategy
   - Mention Time Complexity
   - Mention Space Complexity
   - Mention Applications

6. For programming questions:
   - Explain clearly
   - Give examples when useful

7. Use simple language suitable for university examinations.

8. Structure answers using headings and bullets.

9. Be accurate and concise.

10. If information is uncertain, clearly mention it.
"""

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
            "source": "groq",
            "answer": answer,
            "topic": "General Knowledge",
            "chapter": ""
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
                "Request too large."
            }

        else:

            return {
                "source": "error",
                "answer":
                f"API Error: {e}"
            }

    except Exception as e:

        return {
            "source": "error",
            "answer":
            f"Unexpected Error: {e}"
        }
