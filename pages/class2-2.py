import streamlit as st
import random as r
import menu

menu.menu()
st.title("這是標題")  # 標題
st.write(
    "這是一個用`st.write`顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。"
)
st.write(
    """
這是一個用`st.write`顯示的字串，可以處理 Markdown 語法。
* **粗體文字**
* **斜體文字**
* ~~刪除線~~
* ==螢光筆==
* [連結](https://bracky.streamlit.app/)
* 代碼塊
    ```python
    print("Hello world")
    ```
    """
)

st.write(
    """
# 這是最大標題       
- 這是第一項目
- 這是第二項目
- 這是第三項目
## 這是第二大標題
### 這是第三大標題
#### 這是第四大標題
##### 這是第五大標題
###### 這是第六大標題
         
"""
)
# st.number_input()
# 可以讓使用者輸入數字，設定step=1可以讓使用者只能輸入整數，如果要輸入小數點則設定step=0.1
# min_value=0,max_value=100可以設定最小值和最大值
number = st.number_input("請輸入數字", min_value=0, max_value=100, step=1)
st.write(f"你輸入的數字是{number}")
# value=0可以設定預設值
st.write("---")
# 練習
st.title("練習")
a = st.number_input("請輸入分數", min_value=0, max_value=100, step=1, value=0)
if a >= 90:
    st.write("A")
elif a >= 80:
    st.write("B")
elif a >= 70:
    st.write("C")
elif a >= 60:
    st.write("D")
else:
    st.write("F")
# 按鈕練習
st.write("---")
st.title("###按鈕練習")
# st.button()可以在畫面上顯示一個按鈕，使用者可以點擊按鈕
# key可以設定按鈕的名稱，可以用來區分不同的按鈕
# 如果使用者點擊按鈕，st.button()函數會回傳True，否則回傳False
st.button("點我", key="button1")
if st.button("點我", key="button2"):
    st.balloons()
if st.button("點我", key="button3"):
    st.snow()
# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
st.write(f"存在於session_state的隨機數字={st.session_state.ans}")
st.write("---")
st.write("隨機數字")
# random.randint(1, 100)可以產生一個1到100之間的隨機整數
st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")
if st.button("按我一下", key="random"):
    st.write(f"random.randint(1, 100) = {r.randint(1, 100)}")

# 透過session_state可以在將變數暫時存在瀏覽器當中，直到使用者重新整理整個網頁
# 按下元件、或是與元件互動，都不會讓session_state當中的變數消失
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

st.write(f"存在於session_state的隨機數字={st.session_state.ans}")
