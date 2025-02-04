# 字串格式化
name = "Yun-Tse Kao"
age = 12
print(f"Hello {name} Welcome to python {age}")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示
# 取得字串長度
print(len("Hello world"))  # len()函式可以取得字串的長度
print(len("1"))  # len()函式可以取得字串的長度
# type()函式可以取得型態
print(type("Hello world"))  # str
print(type(1))  # int
print(type(1.0))  # float
print(type(True))  # bool
# 型態轉換
print(int(1.0))  # float轉換成int
print(float("1"))  # int轉換成float
print(str(1))  # int轉換成str
print(str(1.0))  # float轉換成str
print(bool(1))  # int轉換成bool
print(bool(1.0))  # float轉換成bool
print(str(True))  # bool轉換成str
print(str(False))  # bool轉換成str
print(bool("True"))  # str轉換成bool
print(bool("False"))  # str轉換成bool
print(float("1.0"))  # str轉換成float
print(int("1"))  # str轉換成int
print(float("1.0"))  # str轉換成float
# print(int("hello"))  #這行會報錯，因為字串裡面如果有非數字的字元，無法轉換成int

print("輸入開始")
# input()函式可以讀取輸入
# ("")裡面的內容是可以提示訊息會先顯示出來，然後輸入者輸入内容
a = input("請輸入數字:")
print("輸入結束")
print(int(a) + 10)  # 將輸入的字串轉換成int
print(type(a))  # 證明透過input()函式輸入的是字串
a = int(a)
print(type(a))
# 正方形面積
a = int(input("請輸入正方形的邊長:"))
print(a * a)
# 圓面積
a = int(input("請輸入圓的半徑:"))
print(a * a * 3.14)
# 比較運算子
print(1 > 2)  # False
print(1 < 2)  # True
print(1 >= 2)  # False
print(1 <= 2)  # True
print(1 == 2)  # False
print(1 != 2)  # True
# 羅輯運算子
# and運算子
print(True and False)  # False
print(True and True)  # True
print(False and False)  # False
print(False and True)  # False
# or運算子
print(True or False)  # True
print(True or True)  # True
print(False or False)  # False
print(False or True)  # True
# not運算子
print(not True)  # False
print(not False)  # True
# 優先順序
# 1. () 括號
# 2. 次方
# 3. * / // %乘法 除法 整除 取餘數
# 4. 加法減法
# 5 == != > < >= <=比較運算子
# 6 and or not 羅輯運算子
password = input("請輸入密碼:")
if password == "123456":
    print("密碼正確")
elif password == "12345678":
    print("密碼正確")
elif password == "123456789":
    print("密碼正確")
else:
    print("密碼錯誤")
# 連續使用if跟使用elif else的差別
# elif可以排除上一個if的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是使用多個if來獨立判斷，則每個if都會執行，所以效率會較低
