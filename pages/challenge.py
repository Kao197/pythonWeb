import streamlit as st
import random as r
import menu

menu.menu()

if "answer" not in st.session_state:
    st.session_state.answer = r.randrange(0, 101)
if "number2" not in st.session_state:
    st.session_state.number2 = 100
if "number3" not in st.session_state:
    st.session_state.number3 = 0
if "number4" not in st.session_state:
    st.session_state.number4 = 8

n = st.session_state.number4
x = st.session_state.answer
st.title("猜數字小游戲")
e = st.number_input("請輸入數字", min_value=0, max_value=100, step=1, value=0)
if n == 0:
    st.write(f"gg答案是{x}")
elif int(e) == x:
    st.balloons()
    st.write("答對!!!!!")
elif int(e) < x:
    st.write("再大一點!!")
    st.session_state.number4 = st.session_state.number4 - 1
    if st.session_state.number3 < e:
        st.session_state.number3 = e
elif int(e) > x:
    st.write("再小一點!!")
    st.session_state.number4 = st.session_state.number4 - 1
    if st.session_state.number2 > e:
        st.session_state.number2 = e
st.write(f"小於{st.session_state.number2}大於{st.session_state.number3}")
st.write(f"你還有 {st.session_state.number4} 次機會")
if st.button("reset"):
    st.session_state.answer = r.randrange(0, 101)
    st.session_state.number2 = 100
    st.session_state.number3 = 0
    st.session_state.number4 = 8
    st.rerun()
