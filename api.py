# api.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, CI/CD API!")

@app.route('/api/greet/<name>', methods=['GET'])
def greet_name(name):
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(debug=True)
