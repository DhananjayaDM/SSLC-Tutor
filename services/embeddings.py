from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def embed_texts(texts):

    return model.encode(
        texts,
        convert_to_numpy=True
    )