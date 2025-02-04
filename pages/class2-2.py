import streamlit as st

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
==螢光筆==
* [連結](https://bracky.streamlit.app/)
* 代碼塊
    ```python
    print("Hello world")
    ```
    """
)
