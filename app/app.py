import os
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

# Load the model
model_name = os.environ.get('MODEL_NAME', 'all-MiniLM-L6-v2')
model = SentenceTransformer(model_name)

# Create a Flask application
app = Flask(__name__)

# Define a route for the embed endpoint
@app.route('/embed', methods=['POST'])
def embed():
    # Get the sentences from the request JSON
    data = request.get_json()
    sentences = data.get('sentences')

    # Make sure sentences is a list of strings
    if not isinstance(sentences, list) or not all(isinstance(s, str) for s in sentences):
        return jsonify({'error': 'Input should be a list of strings'}), 400

    # Encode the sentences
    embeddings = model.encode(sentences)

    # Return the embeddings as JSON
    return jsonify({'embeddings': embeddings.tolist()})

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')