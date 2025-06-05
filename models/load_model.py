
import tensorflow as tf
import pickle
import os

# Path to model and tokenizer
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.h5')
TOKENIZER_PATH = os.path.join(os.path.dirname(__file__), 'tokenizer.pkl')

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Load the tokenizer
with open(TOKENIZER_PATH, 'rb') as f:
    tokenizer = pickle.load(f)
