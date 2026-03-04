import os

from flask import Flask, jsonify, request
import joblib
import random
import json
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


#load model
model = joblib.load('linear_model.joblib')

@app.route('/',methods=['GET'])
def greeting():
  return "Linear Regression API"

@app.route('/predict/<int:x>',methods=['GET'])
def predict(x):
    try:
        x_value = np.array([[int(x)]])

        prediction = model.predict(x_value)
        prediction = int(round(prediction[0]))

        return jsonify({'expected salary: ':prediction},200) 

    except Exception as e:
        return jsonify({'message':'Invalid data, specify x as an INT!'},400)

@app.errorhandler(404)
def handle_not_found(e):
    return jsonify({
        "message: ": "The requested URL was not found on the server. If you're making a valid request, ensure x is an INT."
    },404)
    

if __name__ == '__main__':
    #run locally
    app.run(debug=True, use_reloader=False)

    #run on render
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
