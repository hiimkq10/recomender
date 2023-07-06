from flask import Flask, jsonify, request
import tensorflow as tf
import os
import random

app = Flask(__name__)
port = int(os.getenv('PORT', 5000))

@app.route('/recommend', methods=['POST'])
def index():
    # Get json input
    data = request.json
    if (data['ids'] is None):
        return {
            'status': 10001,
            'data': None,
            'message': "Data invalid"
        }

    # String array to byte array
    input = []
    for i in data['ids']:
        if (i.strip()):
            input.append(tf.compat.as_bytes(i))
    n = 30
    fill = [b'0'] * n
    random.shuffle(input)
    input = input[:n] + fill[len(input):]

    # Load model and predict 
    model = tf.saved_model.load("")
    _, titles = model([input])

    # Byte array to string array
    predict_arr = []
    for i in tf.keras.backend.get_value(titles[0][:20]):
        predict_arr.append(tf.compat.as_str_any(i))
    result = {
        'status': 400,
        'ids':  predict_arr,
        'message': "SUCCESSFUL"
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
