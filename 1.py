import streamlit as st

#w = float(input('請輸入體重(KG)？'))
w = st.number_input('請輸入體重(KG)？')
h = st.number_input('請輸入身高(M)？')
if confirm_input:
  bmi = w/(h*h)
   #print('BMI為', bmi)
    st.write('BMI為', bmi)
 if (bmi < 18):
    st.write('體重過輕')
 elif (bmi < 24):
     st.write('體重正常')
 elif (bmi < 27):
    st.write('體重過重')
 else:
    st.write('體重肥胖')
