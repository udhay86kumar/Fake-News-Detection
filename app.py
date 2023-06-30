from flask import Flask,render_template,url_for,request
import pandas as pd 
import numpy as np 
import pickle 
import joblib
import nltk
import re
from nltk.stem.porter import PorterStemmer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import one_hot
import keras

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predicter',methods=['POST'])
def predicter():
    if request.method == 'POST':
        data = request.form['News']
        data = str(data)
        onehot_repr1=[one_hot(words,5000)for words in data] 
        embedded_docs1=pad_sequences(onehot_repr1,padding='post',maxlen=20)
        news1 = np.array(embedded_docs1)
        model1 = keras.models.load_model('Lstm.h5')
        pre = model1.predict(news1)
        pre1 = np.where(pre>0.5,1,0)
        np1 = np.argmax(pre1)
        print(np1)
    return render_template('result.html',prediction = np1)
if __name__ == '__main__':
	app.run(debug=True)