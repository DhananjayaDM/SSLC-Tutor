import json

from services.qa_service import answer_question


def retrieve_context(question, topics):

    question = question.lower()

    question_words = []

    for word in question.split():

        word = word.strip(
            ".,?!:;()[]{}\"'"
        )

        if len(word) > 2:
            question_words.append(word)

    scored_topics = []

    for topic in topics:

        searchable_text = f"""
        {topic.get('title', '')}
        {topic.get('original_content', '')}
        {topic.get('notes', '')}
        """.lower()

        score = 0

        for word in question_words:
            score += searchable_text.count(word)

        if score > 0:
            scored_topics.append(
                (score, topic)
            )

    scored_topics.sort(
        key=lambda x: x[0],
        reverse=True
    )

    if not scored_topics:

        print(
            "\nNo matching topic found."
            " Searching complete chapter..."
        )

        context_parts = []

        for topic in topics:

            context_parts.append(
                f"""
TOPIC:
{topic.get('title', '')}

TEXTBOOK CONTENT:
{topic.get('original_content', '')}
"""
            )

        return "\n\n".join(
            context_parts
        )

    print("\nMatched Topics:")

    context_parts = []

    for score, topic in scored_topics[:5]:

        print(
            f"- {topic['title']} "
            f"(score={score})"
        )

        context_parts.append(
            f"""
TOPIC:
{topic.get('title', '')}

TEXTBOOK CONTENT:
{topic.get('original_content', '')}
"""
        )

    return "\n\n".join(
        context_parts
    )


def load_topics():

    with open(
        "generated_notes.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def main():

    topics = load_topics()

    print("=" * 60)
    print("SSLC TUTOR CHATBOT")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        question = input(
            "\nQuestion: "
        ).strip()

        if question.lower() in [
            "exit",
            "quit"
        ]:

            print("Goodbye!")
            break

        context = retrieve_context(
            question,
            topics
        )

        answer = answer_question(
            question,
            context
        )

        print("\nAnswer:")
        print("-" * 60)
        print(answer)
        print("-" * 60)


if __name__ == "__main__":
    main()