import re

def chunk_markdown(content):

    sections = re.split(
        r"^###\s+",
        content,
        flags=re.MULTILINE
    )

    chunks = []

    for section in sections[1:]:

        lines = section.split("\n")

        title = lines[0].strip()

        text = "\n".join(lines[1:])

        chunks.append({
            "title": title,
            "content": text
        })

    return chunks