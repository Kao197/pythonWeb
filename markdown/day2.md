# Python 課程筆記

## 字串格式化

```python
name = "Yun-Tse Kao"
age = 12
print(f"Hello {name} Welcome to python {age}")  # f-string
```

- f-string 可將變數或其他型態的資料放到 `{}`，以顯示在字串中。

## 取得字串長度

```python
print(len("Hello world"))  # 11
print(len("1"))  # 1
```

- `len()` 用於取得字串的長度。

## 型態判斷與轉換

```python
print(type("Hello world"))  # str
print(type(1))  # int
print(type(1.0))  # float
print(type(True))  # bool

print(int(1.0))  # 1
print(float("1"))  # 1.0
print(str(1))  # '1'
print(bool(1))  # True
print(bool(0))  # False
```

- `type()` 可取得變數型態。
- `int()`, `float()`, `str()`, `bool()` 用於型態轉換。

## 輸入與運算

```python
num = int(input("請輸入數字: "))
print(num + 10)
```

- `input()` 用於讀取輸入，並轉換為 `int` 進行運算。

## 計算面積

```python
a = int(input("請輸入正方形邊長: "))
print(a * a)

r = float(input("請輸入圓的半徑: "))
print(r * r * 3.14)
```

- 計算正方形與圓的面積。

## 比較與邏輯運算

```python
print(1 > 2)  # False
print(1 == 2)  # False
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
```

- `and`, `or`, `not` 為邏輯運算子。

## if 條件判斷

```python
password = input("請輸入密碼:")
if password == "123456":
    print("密碼正確")
elif password == "12345678":
    print("密碼正確")
else:
    print("密碼錯誤")
```

- `if-elif-else` 進行條件判斷。

## Streamlit 基礎應用

```python
import streamlit as st

st.title("這是標題")
st.write("這是一個用`st.write`顯示的字串")
```

- `st.title()`: 設定標題。
- `st.write()`: 顯示文字、Markdown。

## Streamlit 輸入與按鈕

```python
number = st.number_input("請輸入數字", min_value=0, max_value=100, step=1)
st.write(f"你輸入的數字是 {number}")

if st.button("點我"):
    st.balloons()
```

- `st.number_input()`: 讓使用者輸入數字。
- `st.button()`: 建立按鈕。

## Streamlit 變數儲存與隨機數

```python
import random as r

if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)

st.write(f"隨機數字: {st.session_state.ans}")
```

- `st.session_state` 可在使用者互動時保留變數。

## Streamlit 猜數字遊戲

```python
if "ans" not in st.session_state:
    st.session_state.ans = r.randint(1, 100)
if "tries" not in st.session_state:
    st.session_state.tries = 7

st.title("猜數字遊戲")
guess = st.number_input("請輸入數字", min_value=0, max_value=100, step=1)
st.write(f"你還有 {n} 次機會")
if st.session_state.tries == 0:
    st.write(f"遊戲結束! 答案是 {st.session_state.ans}")
elif guess == st.session_state.ans:
    st.balloons()
    st.write("答對了!")
elif guess < st.session_state.ans:
    st.write("再大一點!")
    st.session_state.tries -= 1
else:
    st.write("再小一點!")
    st.session_state.tries -= 1
```

- 透過 `st.session_state` 記錄變數，讓遊戲能夠持續進行。
