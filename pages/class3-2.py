import streamlit as st

st.title("數字金字塔")
e = st.number_input("請輸入數字", min_value=1, max_value=9, step=1, value=1)
st.write("數字金字塔")

for i in range(1, e + 1):
    st.write(f"{i}" * i)
st.write("---")
st.title("文字輸入元件")
# st.text_input指令格式 st.text_input(輸入欄位的標題,value="預設顯示文字")
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是:{text}")
