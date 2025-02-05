**Python 課程筆記**

## 1. for 迴圈
- `for` 會搭配 `in` 使用，`in` 後面可接 `list`、`tuple`、`string`、`range()` 等。
- `range(5)` 會產生 `0,1,2,3,4`，不包含 `5`。
- 迴圈內變數可自定義，僅能在迴圈內使用。
- 變數每回合會從範圍內取出一個值。

### 範例：
```python
for i in range(5):
    print(i)
```

- `range(1,5)` 會產生 `1,2,3,4`。
```python
for i in range(1, 5):
    print(i)
```

- `range(1,5,2)` 會產生 `1,3`。
```python
for i in range(1, 5, 2):
    print(i)
```

## 2. `random.randrange()` 函數
- `random.randrange(start, stop, step)` 用於生成範圍內的隨機整數。
```python
import random as r
for i in range(1, 5):
    print(r.randrange(1, 10))
```

## 3. List (列表)
### 建立 List
```python
print([])  # 空列表
print([1, 2, 3])  # 具有三個元素的列表
print([1, 2, 3, ["a", "b", "c"]])  # 巢狀列表
```

### 讀取 List 元素
```python
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[5])  # 'c'
```

### List 長度
```python
print(len(L))  # 6
```

### List 走訪元素
```python
for i in range(len(L)):
    print(L[i])
for i in L:
    print(i)
```

### List 切片
```python
print(L[::2])  # [1,3,'b']
print(L[1:4])  # [2,3,'a']
print(L[1:4:2])  # [2,'a']
```

### List 修改元素
```python
L[0] = 2
print(L)  # [2,2,3,'a','b','c']
```

## 4. Call by Value & Call by Reference
```python
a = 1
b = a
b = 2
print(a, b)  # 1,2
```

```python
a = [1, 2, 3]
b = a
b[0] = 2
print(a, b)  # [2,2,3] [2,2,3]
```

```python
a = [1, 2, 3]
b = a.copy()
b[0] = 2
print(a, b)  # [1,2,3] [2,2,3]
```

## 5. List 操作
### `append()`
```python
L = [1, 2, 3]
L.append(4)
print(L)  # [1,2,3,4]
```

### `remove()`
```python
L = ["a", "b", "c", "d", "a"]
L.remove("a")
print(L)  # ['b','c','d','a']
```

### `pop()`
```python
L.pop(0)  # 移除 index 0 的元素
L.pop()  # 移除最後一個元素
print(L)
```

## 6. Streamlit 應用
### 數字金字塔
```python
import streamlit as st

st.title("數字金字塔")
e = st.number_input("請輸入數字", min_value=1, max_value=9, step=1, value=1)
st.write("數字金字塔")

for i in range(1, e + 1):
    st.write(f"{i}" * i)
```

### 文字輸入元件
```python
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是:{text}")
```

### 讀取 Markdown 檔案
```python
import os
hd_book_files = os.listdir("markdown")
for file_name in hd_book_files:
    with st.expander(file_name[:-3]):
        with open(f"markdown/{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
            st.write(text)
```

