import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

def generate_reply(email):
    if not OPENAI_KEY:
        return f"Hi,\n\nThanks for your message regarding '{email.get('subject')}'. I will review and get back to you shortly.\n\nBest,\nVishal"
    try:
        import openai
        openai.api_key = OPENAI_KEY
        prompt = f"Write a short professional reply to this email:\nSubject: {email.get('subject')}\nBody: {email.get('body')}\nReply:"
        resp = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.2
        )
        return resp.choices[0].text.strip()
    except:
        return f"Hi,\n\nThanks for your message regarding '{email.get('subject')}'. I will review and get back to you shortly.\n\nBest,\nVishal"
