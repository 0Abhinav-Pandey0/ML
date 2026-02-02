import streamlit as st

st.title("My First Streamlit App")
st.write("Hello this is my first app")

""""
Generally we run our python files in terminal 
as python <file_name>

but for streamlit files we run as
streamlit run <file_name>

ie in our case
streamlit run streamlit_test1.py


"""

st.text_input("fixed_acidity","Type Here")

st.button("Predict")