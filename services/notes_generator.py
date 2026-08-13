import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def generate_notes(topic_title, content):

    prompt = f"""
You are an expert SSLC textbook note writer.

Your job is to convert textbook content into high-quality study notes.

TOPIC:
{topic_title}

TEXTBOOK CONTENT:
{content[:5000]}

STRICT RULES:

1. Use ONLY the information available in the textbook content.
2. Do NOT add external knowledge.
3. Do NOT add advanced concepts not present in the content.
4. Do NOT invent facts.
5. Do NOT invent examples.
6. Do NOT answer chapter-end questions.
7. Ignore exercises and question banks.
8. Rewrite the content in simple student-friendly language.
9. Preserve every important fact.
10. Preserve every important definition.
11. Preserve every important reaction.
12. Preserve every important formula.
13. Preserve every important equation.
14. Preserve every important example.
15. Preserve every important application.
16. Preserve every important observation.
17. Preserve every important scientific term.
18. Preserve every important law and principle.
19. Preserve every fact that may be asked in an examination.
20. Do NOT skip small facts.
21. If a fact appears in the textbook, it must appear in the notes.
22. If a reaction appears in the textbook, it must appear in the notes.
23. If a formula appears in the textbook, it must appear in the notes.
24. If an equation appears in the textbook, reproduce it exactly.
25. Do NOT modify chemical equations.
26. Do NOT create new equations.
27. Do NOT create new reactions.
28. Do NOT replace reactions with different reactions.
29. Keep the notes detailed and complete.
30. Remove repetition.
31. Do NOT use markdown code blocks.
32. Do NOT return JSON.
33. Do NOT infer information.
34. Do NOT assume information.
35. Do NOT answer questions found inside the content.
36. Do NOT generate information that is not explicitly present.
37. Do NOT define a term unless the textbook content defines it.
38. Do NOT use your own chemistry, physics, biology, mathematics, social science, or general knowledge.
39. Do NOT complete partially visible equations.
40. Do NOT correct equations.
41. Do NOT explain concepts beyond the textbook content.
42. If information is missing, omit it.
43. If a question appears in the content, do not answer it.
44. Do NOT derive conclusions that are not directly stated.
45. Every statement must be traceable to the provided content.
46. Do NOT generate examples unless explicitly present in the content.
47. Do NOT generate facts from memory.
48. Do NOT generate definitions from memory.
49. Do NOT generate exam answers from memory.
50. Use the textbook content as the ONLY source of truth.

EXAM FACTS REQUIREMENT:

Include all facts that can become:

- MCQ questions
- One-mark questions
- Two-mark questions
- Fill in the blanks
- Very short answer questions

Example:

If the textbook mentions that chip packets contain nitrogen gas,
that fact MUST be included in the notes.

OUTPUT FORMAT:

TOPIC:
{topic_title}

DETAILED NOTES:
Write complete notes.

KEY POINTS:
- Point 1
- Point 2
- Point 3

IMPORTANT FACTS FOR EXAM:
- Fact 1
- Fact 2
- Fact 3

IMPORTANT TERMS:
List only terms explicitly present in the textbook content.

EXAM TIPS:
- Tip 1
- Tip 2
"""

    try:

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=3000
        )

        notes_text = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        return {
            "topic": topic_title,
            "notes": notes_text
        }

    except Exception as e:

        print(
            f"Error generating notes for {topic_title}"
        )

        print(str(e))

        return {
            "topic": topic_title,
            "notes": ""
        }