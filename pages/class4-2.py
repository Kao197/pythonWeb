import streamlit as st  # 匯入 Streamlit 函式庫

# 初始化購物車，確保 `st.session_state.cart` 存在
if "cart" not in st.session_state:
    st.session_state.cart = []

l = st.session_state.cart  # 讓變數 `l` 參考 `st.session_state.cart`，避免重置

# 設定應用標題
st.title("點餐機")

# 建立兩欄佈局，分別用於輸入餐點和加入購物車
col1, col2 = st.columns(2)

with col1:
    a = st.text_input("請輸入餐點")  # 讓使用者輸入餐點名稱

with col2:
    if st.button("加入", key="1"):  # 按下按鈕後，將輸入的餐點加入購物車
        l.append(a)

# 顯示購物車內容
st.write("### 購物車")

# 迭代購物車中的餐點，並提供刪除按鈕
for i in range(len(l)):
    col1, col2 = st.columns(2)  # 每個項目建立兩欄：左側顯示名稱，右側提供刪除按鈕

    with col1:
        st.write(l[i])  # 顯示餐點名稱

    with col2:
        if st.button("刪除", key=f"2{i}"):  # 點擊按鈕刪除對應的餐點
            l.pop(i)  # 移除購物車中的該項目
            st.rerun()  # 重新運行程式，以確保 UI 即時更新
