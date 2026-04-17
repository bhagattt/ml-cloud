from flask import Flask, request, jsonify 
import joblib

application = Flask(__name__)


model = joblib.load('sentiment_model.joblib')

@application.route('/predict', methods=['POST']) 
def predict():
    
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided. Please send a JSON with a "text" key.'}), 400

    # Make a prediction
    prediction = model.predict([text])[0]

    # Return the result 
    return jsonify({
        'input_text': text,
        'sentiment_prediction': prediction
    })

if __name__ == '__main__':
    
    application.run(host='0.0.0.0', port=5000)
