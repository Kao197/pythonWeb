import streamlit as st

st.title("數字金字塔")
e = st.number_input("請輸入數字", min_value=1, max_value=9, step=1, value=1)
st.write("數字金字塔")

for i in range(1, e + 1):
    st.write(f"{i}" * i)
