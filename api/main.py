from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import openai

app = FastAPI()

openai.api_key = "your-api-key"  # Replace this with your real OpenAI key

class GrievanceInput(BaseModel):
    message: str
    tone: Literal["empathetic", "formal", "assertive"]

@app.post("/generate-reply/")
async def generate_reply(input: GrievanceInput):
    prompt = f"""
    Act as an HR support agent. Respond to this grievance in a {input.tone} tone:

    Grievance: {input.message}

    Response:
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        reply = response.choices[0].message["content"].strip()
        return {"reply": reply}

    except Exception as e:
        return {"error": str(e)}
