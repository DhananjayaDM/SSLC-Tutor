def generate_important_points(
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

Extract only the MOST IMPORTANT points required
for competitive exams.

RULES

1. Use ONLY the reference content.
2. Do NOT add outside knowledge.
3. Do NOT generate MCQs.
4. Do NOT generate questions.
5. Do NOT explain in paragraphs.
6. Do NOT rewrite the textbook.
7. Extract the most exam-relevant facts.
8. Keep shortcut keys if present.
9. Keep file extensions if present.
10. Keep formulas if present.
11. Keep memory hierarchies if present.
12. Keep classifications if present.
13. Keep definitions only if important.
14. Maximum 15-20 points.
15. One point per line.

OUTPUT FORMAT

# {topic}

- Point 1
- Point 2
- Point 3
- Point 4

Return only bullet points.
"""

    try:

        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an exam point extractor. "
                        "Return only important points."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=1000,
            temperature=0,
            top_p=0.01
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