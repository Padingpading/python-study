#关键字传参
# 1. 顺序无关：与位置传参不同，关键字传参允许你以任意顺序传递参数，因为每个参数都是通过其名称来识别的。
# 2. 清晰性：关键字传参增加了代码的可读性，因为参数名提供了关于每个参数用途的明确说明。
# 3. 混合使用：在调用函数时，你可以混合使用位置传参和关键字传参，但所有位置传参必须位于关键字传参之前。
# 4. 默认参数：如果函数定义中包含了默认参数，那么在调用函数时，你可以省略这些参数的实参（如果它们使用了默认值）。然而，如果你想要覆盖默认值，你可以通过关键字传参来指定新的值,如果有默认值 则不需要传递参数
# 5. 函数签名：了解函数的签名（即函数定义中形参的列表）对于正确使用键字传参至关重要。如果你尝试传递一个函数签名中不存在的参数名，Python将抛出一个TypeError。
#定义函数
# def function_name(param1, param2, ..., paramN):  
#     # 函数体  
#     pass  
# 调用函数，使用关键字传参  
# function_name(param1=value1, param2=value2, ..., paramN=valueN)

# 定义函数  使用默认值
def greet(name,age, greeting="Hello",school="school"):  
    """  
    使用提供的问候语和名字打招呼  
    """  
    print(f"{greeting},{age}, {name}, {school}!")  
  
# 调用函数，使用关键字传参  
greet("Alice",20,school="school",greeting="Hi")  
  
# 输出: Good morning, Bob!  
  
# 3. 混合使用：在调用函数时，你可以混合使用位置传参和关键字传参，但所有位置传参必须位于关键字传参之前。
greet("Alice",20,school="school",greeting="Hi")  
#greet(name"Alice",20,school="school",greeting="Hi")  
