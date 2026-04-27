import json
from groq import Groq
from app.config import get_settings

settings = get_settings()
client = Groq(api_key=settings.groq_api_key)


def generate_questions(prompt: str) -> dict:
    """
    Calls Groq API with the question generation prompt.
    Uses JSON mode for reliable parsing.
    """
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert CBSE question paper designer. Always return ONLY valid JSON."
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model=settings.groq_model,
            response_format={"type": "json_object"},
            temperature=0.5,
            max_tokens=4096,
        )
        
        raw_text = chat_completion.choices[0].message.content
        return json.loads(raw_text)
        
    except Exception as e:
        raise Exception(f"Groq API Error: {str(e)}")