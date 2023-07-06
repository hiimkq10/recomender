from flask import Flask, jsonify
import tensorflow as tf
import tensorflow_recommenders as tfrs

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5400 }
]

@app.route('/')
def index():
    return jsonify(incomes)

if __name__ == "__main__":
    app.run(debug=False)