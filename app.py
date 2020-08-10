import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app = Flask(__name__)
model = pickle.load(open('C:/Users/rajsu/Desktop/model.pkl', 'rb'))
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    pred = model.predict(final_features)
    return render_template('index.html', prediction_text='The flower is of: {}'.format(pred))

if __name__ == "__main__":  
    app.run(debug=True)