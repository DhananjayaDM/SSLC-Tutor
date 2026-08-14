import os

from dotenv import load_dotenv
from groq import Groq

from services.retriever import (
    retrieve
)

load_dotenv()

client = Groq(
    api_key=os.getenv(
        "GROQ_API_KEY"
    )
)

chapter = input(
    "Chapter: "
).strip()

while True:

    question = input(
        "\nAsk Question: "
    )

    if question.lower() in [
        "exit",
        "quit"
    ]:
        break

    docs = retrieve(
        chapter=chapter,
        query=question,
        k=5
    )

    context = "\n\n".join(
        f"{doc['title']}\n{doc['content']}"
        for doc in docs
    )

    prompt = f"""
You are a Computer Science Tutor.

NOTES:

{context}

QUESTION:

{question}

RULES

1. Answer primarily from notes.
2. If notes are insufficient,
   explain using Computer Science knowledge.
3. Keep explanations useful for exam preparation.
4. Give comparisons when relevant.
5. Mention important exam points when helpful.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("\nAnswer:\n")

    print(
        response
        .choices[0]
        .message
        .content
    )