# for迴迴圈
# for會搭in來使用，in後面接一個有範圍的東西，如list、tuple、string、range等
# range(5)會得到0,1,2,3,4，不包含5
# 迴圈裡的變數可以自取，可是只能在迴圈內使用
# 迴圈變數每回合會從範圍裡取一個資料出來
for i in range(5):
    print(i)
# range可以設定起始值、結束值，但不包含結束值
# range(1,5)會得到1,2,3,4
for i in range(1, 5):
    print(i)
# range可以設定起始值、結束值、間隔直，但不包含結束值
# range(1,5,2)會得到1,3,5
for i in range(1, 5, 2):
    print(i)
# 補充random.randrange(1,100)函數
# random.randrange()函數可以隨機產生一個範圍內的整數
# random.randrange()設定傳入的參數跟range()一樣
import random as r

for i in range(1, 5):
    print(r.randrange(1, 10))
# List 列表\清單\陣列
print([])  # 這是空的List
print([1, 2, 3])  # 這是一個有三個元素的List
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個有六個元素的List
print(1, 2, 3, ["a", "b", "c"])  # 這是一個有六個元素的List
print([1, True, "a", 1.23])  # 這是一個有四個元素的List
# List讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  #'a'
print(L[4])  #'b'
print(L[5])  #'c'
# List取長度，也就是List中有多少個元素，不是indix的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6
# List 走訪元素
# 可以透過取得index的方式來找到List中的資料
# 也可以直接把List當作一個取範圍來取得資料
# 這兩種方式都可以，但是看使用的情境是否會需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]
for i in range(len(L)):
    print(L[i])  # 1,2,3,'a','b','c'
for i in range(0, len(L), 2):  # 0,2,4
    print(L[i])  # 1,3,'b'
for i in L:
    print(i)  # 1,2,3,'a','b','c'
L = [1, 2, 3, "a", "b", "c"]
print(L[::2])  #
# 就是取index 0到最後，每取2個元素，就會得到[1,3,'b']
print(L[1:4])
# 就是取index 1到3的元素，不包含index 4，就會得到[2,3,'a']
print(L[1:4:2])
# 就是取index 1到3的元素，不包含index 4，每次取2個元素，就會得到[2,'a']
# 跟range一樣的用法，只是符號不同
# List修改元素
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2
print(L)  # [2,2,3,'a','b','c']
