import pandas as pd
import numpy as np
import streamlit as st
from prediction import predict

st.title('MPG Prediction App')
st.markdown('This app predicts the **MPG** of a car!')

st.header('Car Features')
col1,col2,col3,col4 = st.columns(4)
with col1:
    cylinders = st.slider('cylinders',2,8,1)
    displacement = st.slider('displacement',50,500,10)
with col2:
      horsepower = st.slider('horsepower',50,500,10)
      weight = st.slider('weight',1500,6000,250)
with col3:
      acceleration = st.slider('acceleration',8,25,1)
      model_year = st.slider('model_year',70,85,70)
with col4:
      origin = st.slider('origin',1,3,1)

if st.button('Predict MPG of Car'):
   result = predict(np.array([[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]]))
   st.text(result[0])
   
