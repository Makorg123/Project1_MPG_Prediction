#pip3 install joblib
import joblib

def predict(data):
   reg = joblib.load('reg_model.sav')
   return reg.predict(data)
