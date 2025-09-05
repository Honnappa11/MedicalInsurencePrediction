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
        
        age=st.text_input('Enter Age')
    with col1:
        sex=st.radio("select Gender :",(" Male","Female"))
        if sex=="Male":
            sex1=0
        else:
            sex1=1
        #sex=st.text_input('If you are Male Please Enter "0" OtherWise "1"')
    
    with col2:
         
         bmi=st.text_input('Enter BMI (Body Mass Index) Value')
    with col2:
        children=st.text_input('Number of Childrens')
    with col1:
        smoker=st.radio("Select :",("Smoker","Non-Smoker"))
        if smoker=="Smoker":
            smoker1=0
        else:
            smoker1=1
        #smoker=st.text_input('If you are Smoker Please Enter "0" Otherwise "1"')
    with col1:
        region=st.radio("select region :",("Southwest 0","Southeast 1","Northwest 2","Norththwest 4"))
        if region=="Southwest 0":
            result=0 
        elif region=="Southeast 1":
            result=1 
        elif region=="Northwest 2":
            result=2 
        else:
            result=3 
            
            
            
       # region=st.text_input('If you are Southwest(0),Southeast(1),Northwest(2),Northeast(3) ')
   
 
    
    # code for prediction
    diagnosis=''
    
    # create the button for prediction
    if st.button('Medical Insurance Cost(Dollars)'):
        diagnosis=prediction_function([age,sex1,bmi,children,smoker1,result])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        