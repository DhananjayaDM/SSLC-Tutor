import faiss
import pickle
import numpy as np

from services.embeddings import (
    embed_texts
)


def retrieve(
    chapter: str,
    query: str,
    k: int = 5
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

    results = []

    for idx in indices[0]:
        if idx == -1:
            continue

        results.append(
            chunks[idx]
        )

    return results