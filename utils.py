from flask import url_for
import tensorflow
import keras
import pathlib
import librosa
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder

ALLOWED_EXTENSIONS = ['wav']

def load_model():
    model = keras.models.load_model("." + url_for('static', filename='models/my_model_ANN_Finall'))
    return model

def predict(filename):
    labelencoder = LabelEncoder()
    labelencoder.classes_ = np.load('static/models/classes.npy')

    model = load_model()

    #preprocess the audio file
    audio, sample_rate = librosa.load(filename, res_type='kaiser_fast') 
    mfccs_features = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
    mfccs_scaled_features = np.mean(mfccs_features.T,axis=0)
    #print(mfccs_scaled_features.shape)

    #Reshape MFCC feature to 2-D array
    mfccs_scaled_features=mfccs_scaled_features.reshape(1,-1)
    #print(mfccs_scaled_features.shape)

    #predicted_label=model.predict_classes(mfccs_scaled_features)
    x_predict=model.predict(mfccs_scaled_features) 
    predicted_label=np.argmax(x_predict,axis=1)
    print(predicted_label)
    prediction_class = labelencoder.inverse_transform(predicted_label) 
    genre = prediction_class[0]
    return genre

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
