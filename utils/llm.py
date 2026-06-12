import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_answer(context, question):

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
    Answer the question using only the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = model.generate_content(
        prompt
    )

    return response.text