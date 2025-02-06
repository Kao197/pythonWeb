**Python Streamlit 欄位與購物車應用課程筆記**

## 1. **Streamlit 欄位元件應用**
### (1) **基本 columns 佈局**
- 使用 `st.columns()` 來建立欄位，分割版面。
- 透過 `key` 設定不同的按鈕 ID。

```python
import streamlit as st

st.title("欄位元件")
col1, col2 = st.columns(2)  # 2 欄
col1.button("按鈕1", key="button1")
col2.button("按鈕2", key="button2")
```

### (2) **自訂欄位寬度**
- 透過 `st.columns([比例])` 調整欄位大小。

```python
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="button3")
col2.button("按鈕2", key="button4")
```

### (3) **多欄位與內部控制**
- 使用 `with colX:` 來在特定欄位內部放置元件。
- 觸發 `st.balloons()` 顯示氣球動畫。

```python
col1, col2 = st.columns([1, 2])
with col1:
    if st.button("按鈕1", key="button8"):
        st.balloons()
    st.write("這是col1")
with col2:
    if st.button("按鈕2", key="button9"):
        st.write("這是col2")
    st.write("這是col2")
```

### (4) **動態欄位數量**
- `st.number_input()` 可讓使用者決定欄位數。
- 迴圈建立對應數量的 `st.button()`。

```python
col_num = st.number_input("請輸入數字", min_value=1)
cols = st.columns(col_num)
for i in range(len(cols)):
    with cols[i]:
        st.button(f"按鈕{i+1}", key=f"button{i+10}")
```

### (5) **按鈕重新整理頁面**
- 使用 `st.rerun()` 來重啟應用。

```python
import time
if st.button("重新整理", key="reset"):
    st.success("準備重新整理")
    time.sleep(3)
    st.rerun()
```

---

## 2. **Streamlit 點餐機應用**
### (1) **初始化購物車**
- `st.session_state` 用於保持購物車內容。

```python
import streamlit as st

if "cart" not in st.session_state:
    st.session_state.cart = []
```

### (2) **建立點餐輸入與按鈕**
- 使用 `st.text_input()` 讓使用者輸入餐點。
- 按鈕觸發 `append()` 將輸入加入購物車。

```python
st.title("點餐機")
col1, col2 = st.columns(2)
with col1:
    a = st.text_input("請輸入餐點")
with col2:
    if st.button("加入", key="1"):
        st.session_state.cart.append(a)
```

### (3) **顯示與刪除購物車內容**
- 透過 `st.write()` 顯示購物車內容。
- 使用 `pop()` 刪除對應項目，並 `st.rerun()` 以更新畫面。

```python
st.write("### 購物車")
for i in range(len(st.session_state.cart)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.cart[i])
    with col2:
        if st.button("刪除", key=f"2{i}"):
            st.session_state.cart.pop(i)
            st.rerun()
```

---

## 3. **Python 基礎字典操作**
### (1) **in 運算符判斷是否存在**
```python
l = [1, 2, 3]
print(1 in l)  # True
print(4 in l)  # False
```

### (2) **字典 `pop()` 方法刪除鍵值對**
- 若 key 存在，返回 value；否則返回預設值。
- 若 key 不存在且無預設值，則報錯。

```python
d = {"a": 5, "b": 10}
print(d.pop("a"))  # 5
print(d.pop("e", "not found"))  # not found
```

### (3) **巢狀字典的存取**
- 透過索引存取字典內部的巢狀資料。

```python
d = {"a": [1, 2, {"e": 40, "f": 50}], "b": {"c": 4, "d": 5}}
print(d["a"]) # [1,2,e:40,f:50]
print(d["a"][0])  # 1
print(d["b"])  # {'c': 4, 'd': 5}
print(d["b"]["c"])  # 4
print(d["a"][2]["f"])  # 50
```

---



