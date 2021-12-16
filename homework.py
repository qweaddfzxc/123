import streamlit as st
you = streamlit_simulation("請輸入剪刀0，石頭1，布2:")
import random 
cp = random.randint(0,2)##生成範圍是0到2的亂數

if(you > 2 or you < 0):
    st.write("沒有這種出法哦")##玩家不能輸入0到2範圍以外的數位
else:
 st.write("電腦出的是 %d\n " % cp)
 if(you == 0):
    if(cp ==  0):
        st.write("平局，請再出一次")
    elif(cp ==  1):
        st.write("你輸了")
    else:
        st.write("你贏了")
 if(you == 1):
    if(cp == 1):
        st.write("平局，請再出一次")
    elif(cp == 2):
        st.write("你輸了")
    else:
        st.write("你贏了")
 if(you == 2):
    if(cp == 2):
         st.write("平局，請再出一次")
    elif(cp == 0):
        st.write("你輸了")
    else:
        st.write("你贏了")
