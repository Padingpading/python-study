# 对列表进行排序
sorted_list = sorted([3, 1, 4, 1, 5, 9, 2])
print(f"Sorted list: {sorted_list}")  # Sorted list: [1, 1, 2, 3, 4, 5, 9]

# 使用key参数进行排序
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
sorted_students = sorted(students, key=lambda student: student[2])  # 按年龄排序
print(f"Sorted students by age: {sorted_students}")
# Sorted students by age: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

#字典根据某个key进行排序,使用sorted,下面的数据变成字典数组
dict = [{"name": "张三", "age": 18}, {"name": "李四", "age": 16}, {"name": "王五", "age": 19}]
sorted_dict = sorted(dict, key=lambda x: x["age"])
print(sorted_dict)


