import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_draft_reply(subject: str, body: str) -> str:
    prompt = f"""
You are an assistant that helps write polite, professional email replies.
Here is the original email:

Subject: {subject}

Body:
{body}

Write a concise, friendly reply draft below:
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert email assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        reply = response.choices[0].message['content'].strip()
        return reply

    except Exception as e:
        print(f"⚠️ Error generating reply: {e}")
        return "(Failed to generate reply)"
