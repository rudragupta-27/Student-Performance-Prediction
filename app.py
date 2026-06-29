import streamlit as st
import joblib
from src.predict import prepare_input

# Page Configuration

st.set_page_config(page_title="Student Performance Prediction",page_icon="🎓",layout="centered")
# Load Saved Objects

model = joblib.load("models/model.pkl")
preprocessor = joblib.load("models/preprocessor.pkl")

# Title

st.title("🎓 Student Performance Prediction")
st.write("Enter the student's details below to predict the student's Math Score.")

# User Inputs

gender = st.selectbox("Gender",["female", "male"])
race = st.selectbox("Race/Ethnicity",["group A","group B","group C","group D","group E",])

parent_education = st.selectbox("Parental Level of Education",["some high school","high school",
        "some college","associate's degree","bachelor's degree","master's degree",])

lunch = st.selectbox("Lunch",["standard","free/reduced",])

test_preparation = st.selectbox("Test Preparation Course",["none","completed",])

reading_score = st.slider("Reading Score",min_value=0,max_value=100,value=50,)

writing_score = st.slider("Writing Score",min_value=0,max_value=100,value=50,)

# Prediction

if st.button("Predict Math Score"):

    input_data = prepare_input(gender,race,parent_education,lunch,test_preparation,reading_score,writing_score,)

    with st.spinner("Predicting..."):

        processed_input = preprocessor.transform(input_data)

        prediction = model.predict(processed_input)

        predicted_score = round(prediction[0], 2)

    st.success(f"🎯 Predicted Math Score: {predicted_score}")