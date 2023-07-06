from flask import Flask, jsonify
import tensorflow as tf

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5400 }
]

@app.route('/')
def index():
    return jsonify(incomes)
