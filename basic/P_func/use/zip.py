# 打包两个列表的元素
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 27, 22]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")
# 输出:
# Alice is 24 years old.
# Bob is 27 years old.
# Charlie is 22 years old.