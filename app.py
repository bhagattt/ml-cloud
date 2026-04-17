from flask import Flask, request, jsonify 

application = Flask(__name__)

@application.route('/')
def home():
    return "API is running", 200

@application.route('/predict', methods=['POST']) 
def predict():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided. Please send a JSON with a "text" key.'}), 400

    # Return the predicted sentiment result
    return jsonify({
        'input_text': text,
        'sentiment_prediction': 'positive',
        'model_version': '1.1'
    })

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5000)
