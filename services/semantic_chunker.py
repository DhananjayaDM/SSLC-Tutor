import json
import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def create_semantic_chunks(text):
    prompt = f"""
You are an educational textbook parser.

Analyze this Class 10 lesson.

Split into meaningful educational topics.

Rules:
1. Do NOT split by page.
2. Do NOT split by character count.
3. One chunk = one concept/topic.
4. Keep complete explanation together.
5. Return ONLY valid JSON.

Format:

[
  {{
    "chapter": "",
    "topic": "",
    "content": ""
  }}
]

Lesson:

{text[:15000]}
"""

    response = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=4000
    )

    content = response.choices[0].message.content.strip()

    print("\n************* RAW LLM RESPONSE *************")
    print(content)
    print("********************************************\n")

    # Remove markdown code blocks if present
    if content.startswith("```"):
        content = content.replace("```json", "")
        content = content.replace("```", "")
        content = content.strip()

    try:
        chunks = json.loads(content)
        return chunks

    except json.JSONDecodeError as e:
        print("JSON Parse Error:", e)
        print("Model Response:")
        print(content)
        return []
