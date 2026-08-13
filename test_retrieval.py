from services.retriever import (
    retrieve
)

results = retrieve(
    "Output"
)

for item in results:

    print("=" * 50)

    print(item["title"])

    print(item["content"])