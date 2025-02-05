**Python 基礎課程筆記**

### 註解與快捷鍵
- `#` 代表註解，不會被執行。
- `Ctrl + ?` 可快速註解或取消註解選取的範圍。

### 基本資料型態與輸出
#### 數字型態
```python
print(1)    # int (整數)
print(1.0)  # float (小數)
```

#### 運算
```python
print(1.0 + 2.0)  # 加法
print(1.0 - 2.0)  # 減法
print(1.0 * 2.0)  # 乘法
print(1.0 / 2.0)  # 除法
```

#### 字串 (string)
```python
print("Hello world")  # 字串
print("Hello world" + "Hello world")  # 字串串接
```

#### 布林值 (Boolean)
```python
print(True)   # 布林值 True
print(False)  # 布林值 False
```

### 變數 (Variables)
```python
a = 10  # 宣告變數 a，賦值為 10
print(a)  # 輸出 10
a = "apple"  # 變數 a 變更為字串 "apple"
print(a)  # 輸出 apple
```

### 運算子 (Operators)
#### 數學運算子
```python
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 整除
print(1 ** 1)  # 次方
print(1 % 1)  # 取餘數
```

#### 運算優先順序
1. `()` 括號內的運算先執行
2. `**` 次方運算
3. `* / // %` 乘法、除法、整除、取餘數
4. `+ -` 加法、減法

#### 字串運算
```python
print("Hello" + "world")  # 字串串接
print("Hello" * 3)  # 字串重複
```