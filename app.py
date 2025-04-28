from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Authority Service is running!"})

@app.route('/protected')
def protected():
    return jsonify({"message": "This is a protected resource."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)