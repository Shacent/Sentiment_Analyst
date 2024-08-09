from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.initializers import Orthogonal
import pickle

app = Flask(__name__)

# Load the sentiment analysis model with custom objects
custom_objects = {'Orthogonal': Orthogonal}
model = load_model('V2_Sentiment_Model.h5', custom_objects=custom_objects)

# Load the tokenizer (pastikan file tokenizer.pkl sudah ada)
with open('V2_tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Define the maximum length for the sequences (sesuaikan dengan model Anda)
maxlen = 41

def preprocess_input(sentence, tokenizer, maxlen):
    sequence = tokenizer.texts_to_sequences([sentence])
    padded_sequence = pad_sequences(sequence, maxlen=maxlen, padding='post')
    return padded_sequence

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    if 'sentence' not in data:
        return jsonify({'error': 'No sentence provided'}), 400
    
    input_sentence = data['sentence']
    
    # Preprocess the input sentence
    preprocessed_input = preprocess_input(input_sentence, tokenizer, maxlen)
    
    # Make a prediction
    prediction = model.predict(preprocessed_input)[0][0]
    
    # Interpret the prediction
    sentiment = 'positive' if prediction >= 0.5 else 'negative'
    
    return jsonify({'sentence': input_sentence, 'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)
