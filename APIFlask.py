import numpy as np
import json
import joblib
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

#Using joblib
model = joblib.load("model.sav")

def model_pred(data_coordinates_array):
    pred = model.predict([np.asarray(data_coordinates_array)])
    return pred


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    data_coordinates_array = json.loads(data)
    prediction = model_pred(data_coordinates_array["dc"])
    # print(data["dc"])
    return jsonify({"Prediction" : prediction[0]})
