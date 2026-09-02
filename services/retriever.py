import os

import faiss
import pickle
import numpy as np

from services.embeddings import embed_texts


STOP_WORDS = {
    "what", "why", "how", "when", "where", "which",
    "who", "whom", "whose",
    "is", "are", "was", "were",
    "be", "been", "being",
    "the", "a", "an",
    "in", "on", "at", "of", "to",
    "for", "from", "with", "than",
    "and", "or", "but",
    "about", "into", "under", "over",
    "through",
    "explain", "define", "describe",
    "discuss", "compare",
    "differentiate", "write",
    "state", "list", "tell", "give"
}


def clean_word(word):

    return word.strip(
        ".,?!:;()[]{}\"'`"
    )


def normalize_word(word):

    word = clean_word(word)
    word = word.lower().strip()

    if word.endswith("ies") and len(word) > 4:
        return word[:-3] + "y"

    if word.endswith("s") and len(word) > 3:
        return word[:-1]

    return word


def normalize_text(text):

    return " ".join(
        normalize_word(word)
        for word in text.split()
    )


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

    query_lower = normalize_text(
        query
    )

    query_words = {
        normalize_word(word)
        for word in query.split()
        if (
            len(clean_word(word)) > 2
            and normalize_word(word)
            not in STOP_WORDS
        )
    }

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

        title = normalize_text(
            get_title(doc)
        )

        text = normalize_text(
            title
            +
            " "
            +
            get_text(doc)
        )

        keyword_score = 0

        #
        # Exact title match
        #

        if title == query_lower:
            keyword_score += 500

        #
        # Title phrase appears in query
        #

        elif title and title in query_lower:
            keyword_score += 200

        #
        # Query phrase appears in content
        #

        if query_lower in text:
            keyword_score += 50

        #
        # Coverage of query words in title
        #

        title_words = {
            normalize_word(word)
            for word in title.split()
        }

        matched_title_words = sum(
            1
            for word in query_words
            if word in title_words
        )

        if query_words:

            coverage = (
                matched_title_words
                /
                len(query_words)
            )

            keyword_score += (
                coverage * 100
            )

        #
        # Content keyword matching
        #

        for word in query_words:

            if word in text:
                keyword_score += 1

        semantic_score = (
            1 / (1 + distance)
        )

        richness_score = min(
            len(text) / 1000,
            1
        )

        final_score = (
            semantic_score * 0.3
            +
            keyword_score * 0.5
            +
            richness_score * 0.2
        )

        doc["semantic_score"] = semantic_score
        doc["richness_score"] = richness_score
        doc["keyword_score"] = keyword_score
        doc["score"] = final_score

        results.append(
            doc
        )

    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


def retrieve_all(
    query: str,
    k: int = 10
):

    all_results = []

    if not os.path.exists(
        "vectordb"
    ):
        return []

    chapters = [
        d
        for d in os.listdir(
            "vectordb"
        )
        if os.path.isdir(
            os.path.join(
                "vectordb",
                d
            )
        )
    ]

    for chapter in chapters:

        try:

            docs = retrieve(
                chapter=chapter,
                query=query,
                k=10
            )

            for doc in docs:

                doc["chapter"] = chapter

                all_results.append(
                    doc
                )

        except Exception:
            continue

    all_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return all_results[:k]