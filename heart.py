import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle




st.image(r"C:\Users\DELL\Pictures\inno_image.webp")
name=st.title('Real-Time Heart Disease Alert')
model=pickle.load(open(r'C:\\Users\\DELL\\Machine Learning\\PHASE-2\\heart.pkl',"rb"))

import streamlit as st

# URL of the background image
background_image_url = "C:\\Users\\DELL\\Pictures\\he-im.jpg"

# Define the custom CSS
page_bg_css = f"""
<style>
body {{
    background-image: url("{background_image_url}");
    background-size: cover;
}}
</style>
"""

# Insert the CSS into the Streamlit app
st.markdown(page_bg_css, unsafe_allow_html=True)
st.image(background_image_url)



st.header('Enter below details')
Age=st.number_input("Enter the Age",min_value = 1, max_value = 100, step = 1)
Gender=st.number_input('Enter the Gender',min_value=0,max_value=1,step=1)
Chest_Pain_Type = st.number_input('Enter the chest pain type', min_value=1, max_value=5, step=1)
Resting_bp_s=st.number_input('Enter the resting bp s',min_value=0,max_value=200,step=1)
Cholesterol=st.number_input('Enter the cholesterol',min_value=0,max_value=700,step=1)
Fasting_blood_sugar =st.number_input('Enter the fasting blood sugar',min_value=0,max_value=1,step=1)
Resting_ecg	=st.number_input('Enter the resting ecg	',min_value=0,max_value=2,step=1)
Max_heart_rate=st.number_input('Enter the max heart rate',min_value=60,max_value=300,step=1)
Exercise_angina=st.number_input('Enter the exercise angina',min_value=0,max_value=1,step=1)
Oldpeak=st.number_input('Enter the oldpeak',min_value=-2.6,max_value=6.2,step=1.0)
ST_slope=st.number_input('Enter the ST slope',min_value=0,max_value=3,step=1)

if st.button("Submit"):
    Heart=model.predict([[Age,Gender,Chest_Pain_Type,Resting_bp_s,Cholesterol,Fasting_blood_sugar,Resting_ecg,Max_heart_rate,Exercise_angina,Oldpeak,ST_slope]])[0]

    if Heart==0:
        st.write('No Disease')
        st.image(r"C:\Users\DELL\Pictures\h-i.jfif",width=600)
    elif Heart==1:
        st.write('Disease')
        st.image(r"C:\Users\DELL\Pictures\ef-im.jpg")
     