import json

from services.pdf_service import (
    save_pages,
    extract_pdf_text
)

from services.general_parser import (
    extract_topics
)

from services.notes_generator import (
    generate_notes
)


def main():

    pdf_path = "data/uploads/acid_base.pdf"

    print("\nSaving pages...")
    save_pages(pdf_path)

    print("\nExtracting text...")
    text = extract_pdf_text(pdf_path)

    print("\nExtracting topics...")
    data = extract_topics(text)

    notes_data = []

    for topic in data["topics"]:

        # Skip chapter headings like 1.1, 1.2, 1.3
        if topic["id"].count(".") < 2:
            continue

        # Skip tiny sections
        if len(topic["content"]) < 150:
            continue

        print(
            f"Generating notes for {topic['title']}"
        )

        notes = generate_notes(
            topic["title"],
            topic["content"]
        )

        notes_data.append({
            "id": topic["id"],
            "title": topic["title"],
            "original_content": topic["content"],
            "notes": notes["notes"]
        })

    with open(
        "generated_notes.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            notes_data,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("\n===================================")
    print("NOTES GENERATED SUCCESSFULLY")
    print("===================================")

    print(
        f"Topics Processed: {len(notes_data)}"
    )

    print(
        "Output File: generated_notes.json"
    )


if __name__ == "__main__":
    main()