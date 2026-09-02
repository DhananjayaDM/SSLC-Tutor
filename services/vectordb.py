import faiss
import pickle
import numpy as np

from services.embeddings import (
    embed_texts
)

def create_db(chunks):

    texts = [
        c["content"]
        for c in chunks
    ]

    embeddings = embed_texts(texts)

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(
        dimension
    )

    index.add(
        embeddings.astype(
            np.float32
        )
    )

    faiss.write_index(
        index,
        "vectordb/05_SQL/index.faiss"
    )

    with open(
        "vectordb/05_SQL/chunks.pkl",
        "wb"
    ) as f:
        pickle.dump(
            chunks,
            f
        )