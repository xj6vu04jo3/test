import streamlit as st

x = st.slider('Select a value')



def BMI(w, h):
    return w/(h*h)

w = st.slider('請輸入體重(KG)？')
h = st.slider('請輸入身高(M)？')
bmi = BMI(w, h)
st.write('BMI為', bmi)
if (bmi < 18):
   st.write('體重過輕')
elif (bmi < 24):
   st.write('體重正常')
elif (bmi < 27):
   st.write('體重過重')
else:
   st.write('體重肥胖')
