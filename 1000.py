import streamlit as st
a = st.number_input('請輸入：1～99 的數字')
confirm_input = st.button('輸入確認')
if confirm_input:
  import random
  b = random.randint(1,99)
  while a!=b:
  if  b < a:
     b = st.write(('數字太小囉！再試一次吧：'))
  elif b > a:
     b = st.write(('數字太大囉！再試一次吧：'))
  else:
     b = st.write('答對囉！');
