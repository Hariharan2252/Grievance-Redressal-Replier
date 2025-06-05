from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from models.load_model import model, tokenizer
from api.templates import CLASS_LABELS, TEMPLATES
import numpy as np
import tensorflow as tf
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GrievanceRequest(BaseModel):
    text: str
    tone: str  # "empathetic", "formal", or "assertive"

@app.post("/generate-reply")
def predict_grievance(request: GrievanceRequest):
    text = request.text
    tone = request.tone.lower()

    # Preprocess
    seq = tokenizer.texts_to_sequences([text])
    padded = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=100)

    # Predict
    prediction = model.predict(padded)
    predicted_class = int(np.argmax(prediction))

    # Lookup label and response
    label = CLASS_LABELS.get(predicted_class, "Unknown")
    response_template = TEMPLATES.get(predicted_class, {}).get(tone, "No response template found for this tone.")
    generated_response = response_template.format(text=text)

    return {
        "predicted_class": predicted_class,
        "predicted_label": label,
        "generated_response": generated_response
    }
