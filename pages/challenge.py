import streamlit as st
import random as r

# 初始化遊戲狀態
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
if "number" not in st.session_state:
    st.session_state.number = 7
if "low" not in st.session_state:
    st.session_state.low = 1
if "high" not in st.session_state:
    st.session_state.high = 100

st.title("猜數字小遊戲")
st.write(f"你還有 {st.session_state.number} 次機會")

# 讓使用者輸入數字
e = st.number_input(
    f"請輸入數字 ({st.session_state.low} ~ {st.session_state.high})",
    min_value=st.session_state.low,
    max_value=st.session_state.high,
    step=1,
    value=st.session_state.low,
)

# 讀取狀態變數
n = st.session_state.number
x = st.session_state.ans

# 遊戲邏輯
if n == 0:
    st.error(f"遊戲結束，答案是 {x}")
elif int(e) == x:
    st.balloons()
    st.success("恭喜答對！")
    st.session_state.ans = r.randint(1, 100)  # 重新開始新遊戲
    st.session_state.number = 7
    st.session_state.low = 1
    st.session_state.high = 100
elif int(e) < x:
    st.warning("再大一點！")
    st.session_state.low = max(st.session_state.low, int(e) + 1)
    st.session_state.number -= 1
elif int(e) > x:
    st.warning("再小一點！")
    st.session_state.high = min(st.session_state.high, int(e) - 1)
    st.session_state.number -= 1
