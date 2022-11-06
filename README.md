<p align="center">
  <img src="https://ichef.bbci.co.uk/images/ic/640x360/p07dzz43.jpg" width="550" title="Music Genre CLassifier">
</p>

A simple Artificial Neural Network that essentially classifies the input song/audio sample into Rock, Classical, Blues, Jazz, Disco, Pop, Metal, Regae, Hiphop or Country.
The model is built on the GTZAN Dataset and provides an accuracy of about 79%

**About the model**

<p align="left">
  <img src="https://miro.medium.com/max/1400/0*BrC7o-KTt54z948C.jpg" width="350" title="Tensorflow & Keras">
</p>

The model is a multilayered ANN build with the help of Keras and Tensorflow. Another important Python library used to play with and for extracting features from the audio file
was Librosa. We have used [Mel Frequency Cepstrum Coefficienct](https://en.wikipedia.org/wiki/Mel-frequency_cepstrum) to convert the extracted features into workable values.

**About the dataset**

<p align="left">
  <img src="https://github.com/9dubs/test/blob/main/dataset.png" width="650" title="Dataset Info">
</p>

The [dataset](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification) was developed by GTZAN and weighs about 1GB in total. It has about 10 
genres, and 100 10 second audio samples for training the model. The extracted features were first preproccessed before actually making use of it to classify the genre.
The Librosa module was essentially used to figure out the MFCC of the input audio sample. 



Please run the ```requirements.txt``` file to get all the dependencies ready for running this application.

Currently the model accepts audio sample **only** in wav format which is indeed quite a restriction but as a beginner, we had to settle for it. We wish to increment the
number of input formats our model accepts, also as a part of our future works.

**This project is still incomplete, and a work in progress**
