import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = model.predict(final_features)

    output = round(pred [0], 3)

    return render_template('index.html', prediction_text = 'Harga termasuk : {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)