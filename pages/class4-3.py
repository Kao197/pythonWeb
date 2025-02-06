# 算數指定運算子
a = 1
a += 1  # a=a+1
print(a)  # 2
a -= 1  # a=a-1
print(a)  # 1
a *= 2  # a=a*2
print(a)  # 2
a /= 2  # a=a/2
print(a)  # 1.0
a //= 2  # a=a//2
print(a)  # 0
a %= 2  # a=a%2
print(a)  # 0.0
a **= 2  # a=a**2
print(a)  # 0.0
# 優先順序
# 1. () 括號
# 2. 次方
# 3. * / // %乘法 除法 整除 取餘數
# 4. 加法減法
# 5. == != > < >= <=比較運算子
# 6. and or not 羅輯運算子
# 7.+= -= *= /= //= %= **=算數指定運算子
# 有儲存會在最後執行
# while迴圈
# while會搭配一個條件式來使用
# 條件式為True時會一直執行迴圈
# 條件式為False時會停止執行迴圈
# 每次迴圈執行完都會重新檢查條件式有沒有變成False
i = 0
while i < 5:
    print(i)
    i += 1  # i=i+1
# break可以強制跳出迴圈
# 先判斷break屬於哪個迴圈，然後跳出哪個迴圈
i = 0
while i < 5:
    print(i)
    for j in range(5):
        print(j)
    if i == 3:
        break  # 強制跳出while迴圈，因為著個break屬於while迴圈
    i += 1
for i in range(5):
    print(i)
    if i == 3:
        break  # 強制跳出for迴圈
# 字典
# dict是透過key-value的方式來儲存資料，key是為一的，value可以重複
# dict是無序的，所以無法透過index方式取得資料
# dict的key必須是不可變的資料型態，例如:int,str,bool,float
# dict的value可以是任意資料型態
# dict的key-value是透過冒號來連接，key:value
# dict的key-value是透過冒號來分隔
d = {"a": 1, "b": 2, "c": 3}
# 取得dict中的key
print(d.keys())  # dict_keys(['a', 'b', 'c'])
for key in d.keys():
    print(key)
# 取得dict中的value
print(d.values())  # dict_values([1, 2, 3])
for value in d.values():
    print(value)
# 取得dict中的key-value
print(d.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])
for key, value in d.items():
    print(key, value)
# 新增/修改dict中的key-value
d["d"] = 4  # 新增
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d["a"] = 5  # 修改
print(d)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# 檢查dict中是否存在某個key
# in不能檢查value，只能檢查key
# 跟list比較，in可以檢查的是list的元素與dict的key
print("a" in d)  # True
print("e" in d)  # False
# list檢查元素
l = [1, 2, 3]
print(1 in l)  # True
print(4 in l)  # False
# 刪除dict中的key-value,pop()方法
# 如果資料有存在，就刪除並回傳value
print(d.pop("a"))  # 5
# 如果資料沒有存在，就回傳預設值
print(d.pop("e", "not found"))  # Not found
# 如果資料不存在也沒有預設值，就會報錯
# 比較複雜的dict
d = {"a": [1, 2, {"e": 40, "f": 50}], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1,2,e:40,f:50]
print(d["a"][0])  # 1
print(d["b"])  # {'c': 4, 'd': 5}
print(d["b"]["c"])  # 4
print(d["a"][2]["f"])  # 50
