import streamlit as st

st.code(
    """
# 這是註解，不會被執行
# ctrl+? 可以把框選的範圍做 快速註解/取消註解
print(1)  # int這是整數，-1,0,1,,2,3,4,5,6,7,8,9,10
print(1.0)  # float這是小數，-1.0,0.0,1.0,,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0
print(1.0 + 2.0)  # 加法
print(1.0 - 2.0)  # 減法
print(1.0 * 2.0)  # 乘法
print(1.0 / 2.0)  # 除法
print("Hello world")  # string這是字串，"Hello world"，"1"也是字串
print("Hello world" + "Hello world")  # 字串加法
print(True)  # bool這是布林值，True,False
print(False)  # bool這是布林值，True,False
print(1 + 1)  # 2
print("1" + "1")  # 11,字串相加是串接
# 變數
a = 10  # 新增一個儲存空間並取名為a
# =的功能是將右邊的值存入左邊的變數
print(a)  # 10
a = "apple"  # 將a的值變成apple
print(a)  # apple
# 運算子
print(1 + 1)  # 加法
print(1 - 1)  # 減法
print(1 * 1)  # 乘法
print(1 / 1)  # 除法
print(1 // 1)  # 整除
print(1**1)  # 次方
print(1 % 1)  # 取餘數
# 優先順序
# 1. () 括號
# 2. 次方
# 3. * / // %乘法 除法 整除 取餘數
# 5. 加法減法
# 字串運算，+、*
print("Hello" + "world")  # 字串相加
print("Hello" * 3)  # 字串乘法

"""
)
