try:
    num = int("abc")
    arr = [1,2]
    print(arr[5])
except ValueError:
    print("数值转换错误")
except IndexError:
    print("列表索引越界")