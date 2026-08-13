import re


def extract_topics(text):

    heading_pattern = re.compile(
        r'^\d+\.\d+(?:\.\d+)?\s+[A-Za-z].*$',
        re.MULTILINE
    )

    matches = list(
        heading_pattern.finditer(text)
    )

    topics = []

    for i, match in enumerate(matches):

        heading = match.group().strip()

        parts = heading.split(" ", 1)

        if len(parts) != 2:
            continue

        topic_id = parts[0]
        topic_title = parts[1].strip()

        # Skip invalid matches
        if (
            "?" in topic_title
            or len(topic_title.split()) > 8
        ):
            continue

        start = match.end()

        if i < len(matches) - 1:
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        # Remove chapter-end content
        stop_words = [
            "QUESTIONS",
            "UESTIONS",
            "EXERCISES",
            "What you have learnt",
            "WHAT YOU HAVE LEARNT"
        ]

        for word in stop_words:

            pos = content.find(word)

            if pos != -1:
                content = content[:pos].strip()

        topics.append({
            "id": topic_id,
            "title": topic_title,
            "content": content
        })

    activities = []

    activity_pattern = re.compile(
        r'^Activity\s+\d+\.\d+$',
        re.MULTILINE | re.IGNORECASE
    )

    for match in activity_pattern.finditer(text):

        activities.append({
            "title": match.group().strip()
        })

    figures = []

    figure_pattern = re.compile(
        r'^Figure\s+\d+\.\d+$',
        re.MULTILINE | re.IGNORECASE
    )

    for match in figure_pattern.finditer(text):

        figures.append({
            "title": match.group().strip()
        })

    return {
        "topics": topics,
        "activities": activities,
        "figures": figures
    }