from flask import Flask
import tensorflow as tf
import os

app = Flask(__name__)
port = int(os.getenv('PORT', 5000))

incomes = [
    { 'description': 'salary', 'amount': 5400 }
]

@app.route('/')
def index():
    model = tf.saved_model.load("")
    scores, titles = model([[b'436', b'155', b'163', b'437', b'237', b'453', b'160', b'435',
      b'152', b'440', b'26', b'130', b'235', b'158', b'152', b'145',
      b'113', b'233', b'146', b'16', b'15', b'86', b'164', b'444',
      b'128', b'113', b'435', b'112', b'440', b'227']])
    print(titles[0][:3])
    return "Hello"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
