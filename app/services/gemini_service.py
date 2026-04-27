import json
from groq import Groq
from app.config import get_settings

settings = get_settings()
# Initialize clients
client1 = Groq(api_key=settings.groq_api_key)
client2 = Groq(api_key=settings.groq_api_key_2) if settings.groq_api_key_2 else None


def generate_questions(prompt: str) -> dict:
    """
    Calls Groq API with the question generation prompt.
    Supports fallback to a second API key if the first one hits a rate limit.
    """
    clients = [client1]
    if client2:
        clients.append(client2)

    last_error = None
    
    for i, client in enumerate(clients):
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
            error_msg = str(e)
            last_error = e
            
            # If it's a rate limit (429) and we have another client, try the next one
            if "429" in error_msg and i < len(clients) - 1:
                print(f"Key {i+1} rate limited. Trying fallback key...")
                continue
            
            # If it's the last client or not a rate limit, raise the error
            raise Exception(f"Groq API Error: {error_msg}")
    
    raise last_error