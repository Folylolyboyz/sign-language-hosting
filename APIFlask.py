import numpy as np
import json
import joblib
from flask import Flask, request

#For image processing on the go

# from flask import flash, redirect, url_for
# from werkzeug.utils import secure_filename
# import os
# import mediapipe as mp
# import cv2 as cv

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
    return json.dumps({"Prediction" : prediction[0]})


#For image processing on the go

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils
# mp_drawing_styles = mp.solutions.drawing_styles
# hands = mp_hands.Hands(static_image_mode = True, min_detection_confidence = 0.3)

# data_coordinates = []
# def landmarks(image_path):
#     image = cv.imread(image_path)
#     image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    
#     output = hands.process(image_rgb)
#     data_coordinates = []
#     if output.multi_hand_landmarks:
#         for hand_landmarks in output.multi_hand_landmarks:
#                 for i in hand_landmarks.landmark:
#                     x = i.x
#                     y = i.y
#                     data_coordinates.append(x)
#                     data_coordinates.append(y)
#         return data_coordinates

# path = "./upload/0.jpg"
# app.config['UPLOAD_FOLDER'] = "./upload"
# @app.route("/image", methods=["POST"])
# def upload_file():
#     file = request.files['image']
#     if file:
#         file.save(os.path.join(app.config['UPLOAD_FOLDER'],"0.jpg"))
#         data_coordinates = landmarks(path)
#         prediction = model_pred(data_coordinates)
#     return json.dumps({"Prediction" : prediction[0]})