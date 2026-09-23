from sentence_transformers import SentenceTransformer

model = None

def get_model():
    global model

    

    return model

def embed_texts(texts):
    return get_model().encode(
        texts,
        convert_to_numpy=True
    )
