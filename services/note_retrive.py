from services.retriever import retrieve
from services.notes_fromchrome import generate_notes

topic = "Memory"

docs = retrieve(
    topic,
    k=3
)

context = "\n\n".join(
    doc["content"]
    for doc in docs
)

notes = generate_notes(
    topic,
    context
)

print(notes)