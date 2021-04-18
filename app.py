import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import cv2
from tensorflow.keras.models import load_model
import os
# load model
Image_model = load_model('CNNmodel.h5')
Image_model.compile(loss = "categorical_crossentropy",
             optimizer = "rmsprop",
             metrics = ["accuracy"])
app = Flask(__name__)
model = pickle.load(open('DecisionModel.pkl', 'rb'))
scale = pickle.load(open('scale.pkl','rb'))
crop = ['Arhar', 'Bajra', 'Barley', 'Coriander', 'Cotton', 'Chillies',
       'Peas', 'Groundnut', 'Jowar', 'Flax', 'Maize', 'Masoor',
       'Moong(green gram)', 'Onion', 'Pulses', 'Potato', 'Ragi',
       'Rapeseed &mustard', 'Rice', 'Safflower', 'Sugarcane', 'Sunflower',
       'Turmeric', 'Urad', 'Wheat', 'Garlic', 'Cowpea', 'Ginger']
classes = ["Pepper bell Bacterial spot",
           "Pepper bell healthy",
           "Potato Early blight",
           "Potato healthy",
           "Potato Late blight",
           "Tomato Bacterial spot",
           "Tomato Early blight",
           "Tomato Late blight",
           "Tomato Leaf Mold",
           "Tomato Septoria leaf spot",
           "Tomato Spider mites Two spotted spider mite",
           "Tomato Target Spot",
           "Tomato YellowLeaf Curl Virus",
           "Tomato mosaic virus",
           "Tomato healthy",
           "Rice Bacterial leaf blight",
           "Rice Brown spot",
           "Rice Leaf smut"
          ]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict1',methods=['POST'])
def predict1():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    features = pd.DataFrame([int_features])
    for i in features.columns:
        # transform the training data column
        features[i] = scale.transform(features[[i]])
    prediction = model.predict([features])
    print(features)
    output = crop[int(prediction[0])]
    print(output)
    return render_template('index.html', prediction_text1='Ideal crop for farming should be {}'.format(output))

'''
'''
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            file_path = os.path.join('C:/Users/jibin/PycharmProjects/Deployment-flask-master/', image.filename)
            image.save(file_path)
        try:
            img = cv2.imread(file_path)
            A1 = cv2.resize(img, (150, 150))
            b1 = np.array(A1.reshape(-1, 150, 150, 3))
            pred = Image_model.predict(b1)
            output1 = (classes[int(pred[0][0])])
        except Exception as e:
            pass

    return render_template('index.html', prediction_text2='The disease classified is {}'.format(output1))



if __name__ == "__main__":
    app.run(debug=True)