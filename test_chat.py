import os
import time

from dotenv import load_dotenv
from groq import Groq
from groq import APIStatusError

from services.retriever import retrieve


load_dotenv()

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
        "alu": "arithmetic logic unit",
        "cu": "control unit",
        "pc": "program counter",
        "ir": "instruction register",
        "mar": "memory address register",
        "mdr": "memory data register",
        "dma": "direct memory access",
        "ram": "random access memory",
        "rom": "read only memory",
        "cache": "cache memory"
    }

    for short, full in replacements.items():

        query = query.replace(
            short,
            full
        )

    return query


chapter = input(
    "Chapter: "
).strip()

print("\nType 'exit' to quit.")

while True:

    question = input(
        "\nAsk Question: "
    ).strip()

    if question.lower() in [
        "exit",
        "quit"
    ]:
        print("\nGoodbye!")
        break

    try:

        query = expand_query(
            question
        )

        docs = retrieve(
            chapter=chapter,
            query=query,
            k=10
        )

        if not docs:

            print(
                "\nInformation not found in the provided notes."
            )

            continue

        print("\nRetrieved Topics:\n")

        for doc in docs[:5]:

            print(
                f"- {get_title(doc)} "
                f"(score={doc.get('score', 0):.3f}, "
                f"distance={doc.get('distance', 0):.3f})"
            )

        best_doc = docs[0]

        print(
            f"\nBest Match: "
            f"{get_title(best_doc)}"
        )

        #
        # Reject completely unrelated queries
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
        # Context from Top 3 Retrieved Notes
        #

        context_parts = []

        for doc in docs[:3]:

            topic = get_title(doc)

            notes = get_text(doc)

            context_parts.append(
                f"TOPIC: {topic}\n\n{notes}"
            )

        context = "\n\n".join(
            context_parts
        )[:4000]

        prompt = f"""
You are an exam preparation assistant.

STUDY NOTES:

{context}

QUESTION:

{question}

RULES:

1. Use the notes as the PRIMARY source.

2. Answer primarily from the notes.

3. You may:
   - simplify explanations
   - provide examples
   - provide worked examples
   - provide truth tables
   - provide exam tips

4. Do not contradict the notes.

5. If information is partially available,
   complete it using standard academic
   computer science knowledge.

6. If information is completely absent,
   say exactly:

   Information not found in the provided notes.

7. Use bullet points whenever useful.

8. Keep answers concise and useful for exams.

9. For binary arithmetic,
   show the complete calculation.

10. For truth tables,
    generate the complete truth table.

11. Maximum 150 words.
"""

        response = (
            client.chat.completions.create(
                model="llama-3.1-8b-instant",
                temperature=0,
                max_tokens=250,
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