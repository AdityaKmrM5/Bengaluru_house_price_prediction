ImportWarning
import dataclasses
import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('random_forest_house_price_model.pkl', 'rb'))

dataset = pickle.load(open('dataset.pkl', 'rb'))

print(type(dataset))

import pandas as pd
dataset = pd.read_pickle('dataset.pkl') 

import pickle

with open("dataset.pkl", "rb") as f:
    dataset = pickle.load(f)

import pandas as pd

dataset = pd.read_csv('Bengaluru_House_Data.csv') 

print(dataset.columns)

dataset.columns = dataset.columns.str.strip() 

dataset = dataset.dropna(subset=['location'])
locations = sorted(dataset['location'].unique())

locations = sorted(dataset['location'].unique())

locations = dataset['location'].unique()

st.title("Blore House Price Prediction")

st.image("House_banner.jpg", use_container_width=True)
location = st.selectbox('Location', locations)
total_sqft = st.number_input('Total Square Foot', min_value=0.0, value=1000.0)
col1, col2 = st.columns(2)
with col1:
    bath = st.number_input('Number of Bathrooms', min_value=1, max_value=10, value=2)
with col2:
    bhk = st.number_input('Number of Bedrooms (BHK)', min_value=1, max_value=10, value=2)
    area_types = sorted(dataset['area_type'].dropna().unique())
area_type = st.selectbox('Area Type', area_types)



st.title(" Bangalore House Price Prediction")
st.markdown("Get an instant estimate for your dream home  ")
if st.button('Predict'):
    input_data = pd.DataFrame([{
        'location': location,
        'total_sqft': total_sqft,
        'bath': bath,
        'bhk': bhk,
        'area_type': area_type
    }])
    
    prediction = model.predict(input_data)[0]

    st.markdown("##  Predicted Price")
    st.success(f" ₹ {prediction:.2f} lakhs")


st.markdown("""
> Turning ideas into reality, one prediction at a time.
""")