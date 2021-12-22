import streamlit as st
a = st.number_input('請輸入：1～99 的數字')
confirm_input = st.button('輸入確認')
confirm_input = random.randint(1,99)
while True:
  if  confirm_input< a:
    confirm_input = st.write(('數字太小囉！再試一次吧：'))
  elif confirm_input > a:
    confirm_input = st.write(('數字太大囉！再試一次吧：'))
  else:
    st.write('答對囉！');
