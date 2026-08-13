import faiss
import pickle
import numpy as np

from services.embeddings import (
    embed_texts
)

index = faiss.read_index(
    "vectordb/index.faiss"
)

with open(
    "vectordb/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)


def retrieve(
    query: str,
    k: int = 3
):

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