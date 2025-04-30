# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:15:45 2025

@author: HONNAPPA M S
"""

import pickle
import numpy as np
import streamlit as st

load_model=pickle.load(open('C:/Users/HONNAPPA M S/Desktop/Medical Insurance Prediction/medical_insurance_data.sav','rb'))

# create function for prediction
def prediction_function(input):
    
# converting data into as nparray
    input_data_asarray=np.asarray(input,dtype=np.float32)
# array as reshaped
    input_data_reshaped=input_data_asarray.reshape(1,-1)
    predict=load_model.predict(input_data_reshaped)
    return predict


def main():
    
    # creating title
    st.title('Medical Insurance Cost Prediction using  ML')
    
  #age', 'sex', 'bmi', 'children', 'smoker', 'region
  #'region':{'southwest':0,'southeast':1,'northwest':2,'northeast':3
    #getting the input from user
    
    col1,col2=st.columns(2)
    
    with col1:
        
        age=st.text_input('Enter you are Age')
    with col2:
        sex=st.text_input('If you are Male Please Enter "0" OtherWise "1"')
    
    with col1:
         
         bmi=st.text_input('Enter the BMI Value')
    with col2:
        children=st.text_input('Number of Childrens')
    with col1:
        smoker=st.text_input('If you are Smoker Please Enter "0" Otherwise "1"')
    with col1:
        region=st.text_input('If you are Southwest(0),Southeast(1),Northwest(2),Northeast(3) ')
   
 
    
    # code for prediction
    diagnosis=''
    
    # create the button for prediction
    if st.button('Medical Insurance Cost Result'):
        diagnosis=prediction_function([age,sex,bmi,children,smoker,region])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        