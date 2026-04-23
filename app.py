import streamlit as st
import numpy as np
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

import pickle
model = pickle.load(open('gb_model.pkl', 'rb'))

st.title('Insurance Price Prediction')

#define inputs to take inputs from user
age = st.number_input('Age',min_value=1, max_value=100,value=25)
gender = st.selectbox('Gender',('Male','Female'))
bmi = st.number_input('BMI',min_value=10.0, max_value=80.0,value=30.0)
children = st.number_input('Children',min_value=0, max_value=10,value=2)
smoker = st.selectbox('Smoker',('Yes','No'))
region = st.selectbox('Region',('Southwest','Southeast','Northwest','Northeast'))

#Encoding Techniques
#Smoker
Smoker = 1 if smoker == 'Yes' else 0
#Gender
sex_male = 1 if gender == 'Male' else 0
sex_female = 1 if gender == 'Female' else 0

#Region
region_dict = {'Southwest':0,'Southeast':3,'Northwest':1,'Northeast':2}
Region = region_dict[region]

#create dataframe
input_features = pd.DataFrame({
    'age':[age],
     'bmi':[bmi],
     'children':[children],
     'Smoker':[Smoker],
     'sex_female':[sex_female],
     'sex_male':[sex_male],
     'Region':[Region]
    })

scaler = StandardScaler()
input_features[['age','bmi']] = scaler.fit_transform(input_features[['age','bmi']])

#predictions
if st.button('Predict'):
  predictions = model.predict(input_features)
  output = round(np.exp(predictions[0]),2)
  st.success(f'The insurance price Prediction : ₹ {output}')