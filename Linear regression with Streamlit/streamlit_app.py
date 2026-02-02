"""
Linear regression model for predicting wine quality.

Created on Sunday Feb 2 2025

@ Author: Abhinav Pandey

"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

from PIL import Image

pickle_in = open("linear_wine_model.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    st.title("Wine Quality Prediction")
    st.text("Predict the quality of wine based on its features.")
    return "Welcome to Wine Quality Prediction App"

def predict_wine_quality(fixed_acidity, volatile_acidity, citric_acid, residual_sugar,
                                 chlorides, free_sulfur_dioxide, total_sulfur_dioxide,
                                 density, pH, sulphates, alcohol):
    prediction = classifier.predict([[fixed_acidity, volatile_acidity, citric_acid,
                                      residual_sugar, chlorides, free_sulfur_dioxide,
                                      total_sulfur_dioxide, density, pH,
                                      sulphates, alcohol]])
    print(prediction)
    return prediction

def main():
    st.title("Wine Quality Prediction App")

    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Wine Quality Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    fixed_acidity = st.text_input("Fixed Acidity", "Type Here")
    volatile_acidity = st.text_input("Volatile Acidity", "Type Here")
    citric_acid = st.text_input("Citric Acid", "Type Here")
    residual_sugar = st.text_input("Residual Sugar", "Type Here")
    chlorides = st.text_input("Chlorides", "Type Here")
    free_sulfur_dioxide = st.text_input("Free Sulfur Dioxide", "Type Here")
    total_sulfur_dioxide = st.text_input("Total Sulfur Dioxide", "Type Here")
    density = st.text_input("Density", "Type Here")
    pH = st.text_input("pH", "Type Here")
    sulphates = st.text_input("Sulphates", "Type Here")
    alcohol = st.text_input("Alcohol", "Type Here")

    result = ""

    if st.button("Predict"):
        result = predict_wine_quality(float(fixed_acidity), float(volatile_acidity),
                                      float(citric_acid), float(residual_sugar),
                                      float(chlorides), float(free_sulfur_dioxide),
                                      float(total_sulfur_dioxide), float(density),
                                      float(pH), float(sulphates), float(alcohol))
        st.success(f'The predicted wine quality is: {result[0]}')

    if st.button("About"):
        st.text("Developed by Abhinav Pandey")

if __name__ == '__main__':

    main()
