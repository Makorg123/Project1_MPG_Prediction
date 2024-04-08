import pandas as pd
import numpy as np
import streamlit as st
from prediction import predict

st.title('MPG Prediction App')
st.markdown('This app predicts the **MPG** of a car!')

st.header('Car Features')
col1,col2,col3,col4 = st.columns(4)
with col1:
    cylinders = st.slider('cylinders',3,8,3)
    displacement = st.slider('displacement',68,455,10)
with col2:
      horsepower = st.slider('horsepower',46,230,10)
      weight = st.slider('weight',1500,5200,100)
with col3:
      acceleration = st.slider('acceleration',8,25,1)
      model_year = st.slider('model_year',70,85,70)
with col4:
      origin = st.slider('origin: 1-USA, 2-EU, 3-Asia',1,3,1)

if st.button('Predict MPG of Car'):
   result = predict(np.array([[cylinders,displacement,horsepower,weight,acceleration,model_year,origin]]))
   formatted_result = "{:.2f}".format(result[0])
   st.text('The predicted MPG of the car is: ' + formatted_result)
   
