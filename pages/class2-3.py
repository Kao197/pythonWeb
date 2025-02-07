import streamlit as st
import random as r

if "ans" not in st.session_state:
    st.session_state.ans = r.randrange(1, 101)
if "number" not in st.session_state:
    st.session_state.number = 7
n = st.session_state.number
x = st.session_state.ans
st.title("猜數字小游戲")
e = st.number_input("請輸入數字", min_value=0, max_value=100, step=1, value=0)
st.write(f"你還有 {n} 次機會")

if n == 0:
    st.write(f"gg答案是{x}")
if int(e) == x:
    st.balloons()
    st.write("答對!!!!!")
elif int(e) < x:
    st.write("再大一點!!")
    st.session_state.number = st.session_state.number - 1
elif int(e) > x:
    st.write("再小一點!!")
    st.session_state.number = st.session_state.number - 1
