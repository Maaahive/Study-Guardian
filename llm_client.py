import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY not found in environment variables.")

genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

def generate_text(prompt: str, system_instruction: str | None = None) -> str :
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=system_instruction or "You are a helpful study assistant."
    )

    response = model.generate_content(prompt)
    return response.text