from flask import Flask

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5400 }
]

@app.route('/')
def index():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=False)
