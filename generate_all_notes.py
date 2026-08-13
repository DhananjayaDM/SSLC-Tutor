import json
import pickle

from services.notes_fromchrome import (
    generate_notes
)

with open(
    "vectordb/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)

notes_data = []

for chunk in chunks:

    topic = chunk["title"]

    context = chunk["content"]

    print(
        f"Generating notes for: {topic}"
    )

    notes = generate_notes(
        topic,
        context
    )
    print(notes)

    notes_data.append({
        "topic": topic,
        "notes": notes
    })

with open(
    "Fundamentals_of_Computers.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        notes_data,
        f,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Generated {len(notes_data)} topics"
)