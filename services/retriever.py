import faiss
import pickle
import numpy as np

from services.embeddings import embed_texts


def get_text(doc):

    return (
        doc.get("content", "")
        +
        " "
        +
        doc.get("notes", "")
    )


def get_title(doc):

    return (
        doc.get("title")
        or doc.get("topic")
        or ""
    )


def retrieve(
    chapter: str,
    query: str,
    k: int = 10
):

    index = faiss.read_index(
        f"vectordb/{chapter}/index.faiss"
    )

    with open(
        f"vectordb/{chapter}/chunks.pkl",
        "rb"
    ) as f:

        chunks = pickle.load(f)

    query_embedding = embed_texts(
        [query]
    )

    distances, indices = index.search(
        query_embedding.astype(
            np.float32
        ),
        k
    )

    query_words = set(
        word.lower()
        for word in query.split()
        if len(word) > 2
    )

    results = []

    for distance, idx in zip(
        distances[0],
        indices[0]
    ):

        if idx == -1:
            continue

        doc = chunks[idx].copy()

        doc["distance"] = float(
            distance
        )

        text = (
            get_title(doc)
            +
            " "
            +
            get_text(doc)
        ).lower()

        keyword_score = 0

        for word in query_words:

            if word in text:
                keyword_score += 1

        doc["keyword_score"] = (
            keyword_score
        )

        #
        # Hybrid Score
        #

        semantic_score = (
            1 / (1 + distance)
        )

        final_score = (
            semantic_score * 0.7
            +
            keyword_score * 0.3
        )

        doc["score"] = final_score

        results.append(
            doc
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results