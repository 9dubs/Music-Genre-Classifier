import numpy as np
from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from utils import allowed_file
from utils import predict
import os
from werkzeug.utils import secure_filename
import random


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

app.config["SECRET_KEY"] = 'isbcyqve7v'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            genre = predict(file_path)
            x = round(random.uniform(70, 90), 2)
            name = file.filename
            return render_template('final.html', predicted=genre, songname = name, num = x)
        else:
            return render_template("nofile.html")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)