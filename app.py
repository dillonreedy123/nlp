from flask import Flask, request, jsonify
from classify_sentiment import classify_text

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/api/sentiment', methods=['GET', 'POST'])
def post_sentiment():
    print(request)
    text = request.json['text']
    sentiment = classify_text(text)
    print(sentiment)
    return jsonify(sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')