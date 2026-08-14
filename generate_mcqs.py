import os
import json
import pickle

from services.mcq_generator import (
    generate_mcqs
)

os.makedirs(
    "mcqs",
    exist_ok=True
)

with open(
    "vectordb/chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)

for chunk in chunks:

    topic = chunk["title"]

    context = chunk["content"]

    print(
        f"Generating MCQs for: {topic}"
    )

    response = generate_mcqs(
        topic,
        context
    )

    if not response:

        continue

    file_name = (
        topic
        .replace(" ", "_")
        .replace("/", "_")
        .replace("\\", "_")
    )

    try:

        data = json.loads(
            response
        )

        with open(
            f"mcqs/{file_name}.json",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"Saved: mcqs/{file_name}.json"
        )

    except Exception as e:

        print(
            f"JSON parse error for {topic}: {e}"
        )

print(
    "\nAll MCQ files generated."
)