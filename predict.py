import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer
with open('models/tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

# Load trained RNN model
model = load_model('models/grievance_rnn_model.h5')

# Define max sequence length (same as training)
MAX_SEQUENCE_LENGTH = 50  # Update this if different in your training

# Input text to predict
input_text = input("Enter a grievance: ")



# Tokenize and pad
seq = tokenizer.texts_to_sequences([input_text])
padded_seq = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)

# Predict
prediction = model.predict(padded_seq)

print("Prediction output:", prediction)

import numpy as np

# Get index of highest probability
predicted_class = np.argmax(prediction)
print("Predicted class index:", predicted_class)

# If you have class labels, map it:
class_labels = ['Payroll', 'Leave', 'Policy', 'Harassment', 'Workload', 'Promotion', ...]  # Add actual categories
print("Predicted category:", class_labels[predicted_class])

