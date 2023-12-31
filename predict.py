#creating the UI of model using strealit

import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tokenizer import tokenizer , max_lenght , trunc_type
import streamlit as st
import numpy as np

st.title("IMDB Sentiment Analysis")
st.write("Hello everyone!"
         "Please enter your review below for sentiment analysis")
with st.spinner("Loading Model....."):
    new_model = tf.keras.models.load_model('model/sentiment-analysis-model.h5')

pred_review_text = st.text_input("Enter your review")

if pred_review_text != '':
    pred = []
    pred.append(pred_review_text)

    with st.spinner("Tokenizing Text....."):
        pred_seq = tokenizer.texts_to_sequences(pred)
        pred_padded = pad_sequences(pred_seq, maxlen=max_lenght, truncating=trunc_type)

    val = new_model.predict(pred_padded)
    new_val = str(val)
    st.subheader("The given review was : ")
    if val > [[0.5]]:
        st.write("Positive")
    else:
        st.write("Negative")









