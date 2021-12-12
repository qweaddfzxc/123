import streamlit as st
user1 = st.number_input("請輸入：剪刀：（0）、石頭（1）、布（2）")
user1 = st.button('輸入確認')
import random as rd
computer = random.randint(0,2)
if user1 == computer:
    if user1==0:
        st.write("你的輸入為：剪刀（0）")
        st.write("隨機生成數字為：0")
    elif user1==1:
        st.write("你的輸入為：石頭（1）");
        st.write("隨機生成數字為：1");
    else:
        st.write("你的輸入為：布（2）");
        st.write("隨機生成數字為：2");
    st.write("啊哈，是平局！");
elif user1 == 0 and computer == 1:
    st.write("你的輸入為：剪刀（0）");
    rd.write("隨機生成數字為：1");
    st.write(("哈哈，你輸了"));
elif user1 == 0 and computer == 2:
    st.write("你的輸入為：剪刀（0）");
    rd.write("隨機生成數字為：2");
    st.write(("恭喜你贏啦！"));
elif user1 == 1 and computer == 0:
    st.write("你的輸入為：石頭（1）");
    rd.write("隨機生成數字為：0");
    st.write(("恭喜你贏啦！"));
elif user1 == 1 and computer == 2:
    st.write("你的輸入為：石頭（1）");
    rd.write("隨機生成數字為：2");
    st.write(("哈哈，你輸了"));
elif user1 == 2 and computer == 0:
    st.write("你的輸入為：布（2）");
    rd.write("隨機生成數字為：0");
    st.write(("哈哈，你輸了"));
elif user1 == 2 and computer == 1:
    st.write("你的輸入為：布（2）");
    rd.write("隨機生成數字為：1");
    st.write(("恭喜你贏啦"));
