import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_mcqs(
    topic: str,
    content: str
):

    prompt = f"""
You are a Senior Computer Science
Competitive Examination Paper Setter.

You have experience creating questions for:

- KSET
- UGC NET
- Government Recruitment Exams
- Computer Operator Exams
- Technical Aptitude Tests
- University Entrance Examinations

=================================================
TOPIC
=================================================

{topic}

=================================================
SYLLABUS CONTENT
=================================================

{content}

=================================================
MISSION
=================================================

The supplied content defines ONLY the syllabus
boundary.

The content is NOT a source from which every
sentence should become a question.

You are acting as a REAL examiner.

Create questions that could genuinely appear
in a competitive Computer Science examination.

=================================================
HOW TO THINK
=================================================

Do NOT think like a teacher.

Do NOT think like a textbook author.

Do NOT think like a note writer.

Think like:

- KSET examiner
- Recruitment examiner
- UGC NET examiner

=================================================
FIRST IDENTIFY
=================================================

Before creating any question identify:

- Concepts
- Components
- Features
- Comparisons
- Hierarchies
- Classifications
- Applications
- Confusions
- Frequently misunderstood facts

Generate questions from concepts.

NOT from sentences.

=================================================
STRICTLY REJECT
=================================================

Reject questions such as:

❌ What is RAM?

❌ What is ROM?

❌ What is Keyboard?

❌ What is Scanner?

❌ Which is an Input Device?

❌ Which is an Output Device?

❌ Example of RAM?

❌ Example of ROM?

❌ Example of HDD?

❌ Purpose of Keyboard?

❌ Purpose of Scanner?

❌ Purpose of Mouse?

❌ Which device is a Monitor?

These are weak questions.

=================================================
PREFERRED QUESTION TYPES
=================================================

Generate mostly:

✅ Which statement is correct?

✅ Which statement is NOT correct?

✅ Which of the following is NOT...

✅ Which pair is correctly matched?

✅ Which pair is incorrectly matched?

✅ Classification questions

✅ Comparison questions

✅ Application questions

✅ Memory hierarchy questions

✅ Confusion questions

✅ Examiner trap questions

✅ Conceptual questions

=================================================
DO NOT GENERATE
=================================================

Avoid:

❌ Importance rankings

❌ Complexity rankings

❌ Popularity rankings

❌ Capacity rankings

❌ Assumed speed rankings

❌ Undefined orderings

Unless explicitly mentioned in content.

=================================================
QUESTION VALIDATION
=================================================

Before accepting each question verify:

1. Exactly one answer is correct.

2. No factual error exists.

3. No duplicate question exists.

4. No repeated concept exists.

5. Question is not trivial.

6. Question is not obvious.

7. Question can realistically appear
   in a competitive exam.

8. Distractors are plausible.

If validation fails:

Reject the question.

Generate a better one.

=================================================
DIFFICULTY DISTRIBUTION
=================================================

Easy      20%

Medium    50%

Hard      30%

=================================================
QUESTION COUNT
=================================================

Tiny Topic:
5 to 8 Questions

Medium Topic:
8 to 12 Questions

Large Topic:
10 to 15 Questions

Generate fewer but stronger questions.

Never increase question count using
weak questions.

=================================================
OUTPUT FORMAT
=================================================

Return ONLY valid JSON.

No markdown.

No explanation.

No text before JSON.

No text after JSON.

Format:

{{
  "topic": "{topic}",
  "total_questions": 0,
  "mcqs": [
    {{
      "question": "",
      "options": [
        "",
        "",
        "",
        ""
      ],
      "answer": "",
      "difficulty": "medium",
      "type": "conceptual"
    }}
  ]
}}
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            temperature=0.1,
            max_completion_tokens=1800,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a Computer Science
competitive examination paper setter.

Generate only high-quality questions.

Reject:
- definition questions
- example-based questions
- identification questions
- textbook questions
- trivial questions

Generate:
- conceptual questions
- comparison questions
- classification questions
- elimination questions
- application questions
- examiner trap questions

Quality > Quantity.

Return valid JSON only.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        content = (
            content
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        start = content.find("{")
        end = content.rfind("}")

        if start != -1 and end != -1:
            content = content[start:end + 1]

        return content

    except Exception as e:

        print(
            f"Error generating MCQs: {e}"
        )

        return None