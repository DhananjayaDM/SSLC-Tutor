import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_notes(
    topic: str,
    context: str
):

    prompt = f"""
You are a Competitive Exam Trainer.

TOPIC:
{topic}

REFERENCE CONTENT:
{context}

TASK

Create concise, exam-oriented revision notes from
the given content.

ALLOWED

1. Reorganize content.
2. Convert paragraphs into bullet points.
3. Merge duplicate information.
4. Improve readability.
5. Highlight exam-relevant facts.
6. Simplify wording.
7. Extract important concepts.
8. Group related facts.

NOT ALLOWED

1. Add new topics.
2. Add new subtopics.
3. Add outside knowledge.
4. Add facts not present in the content.
5. Add technologies not mentioned.
6. Add new examples.
7. Add new shortcut keys.
8. Add new file extensions.
9. Add new classifications.
10. Add future predictions.
11. Add historical details not present.
12. Generate MCQs.
13. Generate questions.
14. Generate answers.

VERY IMPORTANT

Preserve whenever present:

- Definitions
- Characteristics
- Features
- Types
- Classifications
- Components
- Examples
- Applications
- Steps
- Memory Hierarchies
- Comparisons
- Shortcut Keys
- File Extensions
- Formulas
- Function Names
- Operating System Examples

PRIORITY ORDER

1. Definitions
2. Characteristics
3. Types
4. Components
5. Examples
6. Shortcut Keys
7. File Extensions
8. Memory Hierarchies
9. Comparisons
10. Exam Facts

OUTPUT RULES

- Maximum 20 important points.
- One point per line.
- Avoid long paragraphs.
- Keep points directly useful for revision.
- Do not include introductory text like:
  "Here are the notes..."
- Start directly with the topic heading.

OUTPUT FORMAT

# {topic}

- Point 1
- Point 2
- Point 3

Return ONLY the notes.
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert Competitive Exam Revision
Notes Generator.

Your responsibility is to:

- Extract exam-important facts.
- Preserve syllabus accuracy.
- Improve readability.
- Never introduce new syllabus content.
- Never hallucinate.
- Never expand the scope of the topic.
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_completion_tokens=1200
        )

        return (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

    except Exception as e:

        print(
            f"Error generating points: {e}"
        )

        return ""