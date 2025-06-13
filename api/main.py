from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from models.load_model import model, tokenizer, label_encoder, tone_encoder, department_encoder
from api.templates import TEMPLATES
import numpy as np
import tensorflow as tf

app = FastAPI()

# CORS config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GrievanceRequest(BaseModel):
    text: str

@app.post("/generate-reply")
def generate_reply(request: GrievanceRequest):
    text = request.text.strip()

    # Preprocess input
    seq = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=50)

    # Predict tone, department, label
    tone_pred, dept_pred, label_pred = model.predict(padded)

    # Decode predictions
    tone = tone_encoder.inverse_transform([np.argmax(tone_pred)])[0].lower()
    department = department_encoder.inverse_transform([np.argmax(dept_pred)])[0].lower()
    label = label_encoder.inverse_transform([np.argmax(label_pred)])[0].lower()

    # Fetch template
    response = "We received your grievance. Thank you for reaching out."
    label_templates = TEMPLATES.get(label, {})
    tone_templates = label_templates.get(tone, {})

    if tone_templates and department in tone_templates:
        template = tone_templates[department]
        response = template.format(text=text)
    elif tone_templates:
        # Use any available department's template
        template = next(iter(tone_templates.values()))
        response = template.format(text=text)

    return {
        "reply": response,
        "predicted_label": label,
        "predicted_tone": tone,
        "predicted_department": department
    }
