import tensorflow as tf
import pickle
from tensorflow.keras.models import load_model
from pathlib import Path

# Set base path to models/ folder
base_path = Path(__file__).parent

# Load the trained multi-output model
model = load_model(base_path / "grievance_multi_output_model.h5")

# Load the tokenizer
with open(base_path / "tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

# Load all three encoders: tone, department, label
with open(base_path / "encoders.pkl", "rb") as handle:
    encoders = pickle.load(handle)
    tone_encoder = encoders["tone"]
    department_encoder = encoders["department"]
    label_encoder = encoders["label"]
