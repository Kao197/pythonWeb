import streamlit as st

if "cart" not in st.session_state:
    st.session_state.cart = []
l = st.session_state.cart
st.title("點餐機")
col1, col2 = st.columns(2)
cols = st.columns(2)
with col1:
    a = st.text_input("請輸入餐點")
with col2:
    if st.button("加入", key="1"):
        l.append(a)
st.write("### 購物車")
for i in range(len(l)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(l[i])
    with col2:
        if st.button("刪除", key=f"2{i}"):
            l.pop(i)
            st.rerun()
