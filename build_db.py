from pathlib import Path

from services.chunker import (
    chunk_markdown
)

from services.vectordb import (
    create_db
)

text = Path(
    "knowledge_base/10_Artificial_Neural_Networks.md"
).read_text(
    encoding="utf-8"
)

chunks = chunk_markdown(
    text
)

create_db(chunks)

print("Vector DB Created")