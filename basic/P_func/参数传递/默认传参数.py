#默认参数:在函数定义时，你可以通过为参数分配一个默认值来创建默认参数。
#这个默认值可以是任何静态值，包括数字、字符串、列表、元组、字典、集合、None等，
#但不能是变量（因为变量在函数定义时可能尚未定义或已被赋予不同的值）。 
#1.定义
# def function_name(param1, param2=default_value2, ..., paramN=default_valueN):  
#     # 函数体  
#     pass

# 定义函数，其中一个参数有默认值  
def greet(name, greeting="Hello",age=12,school=['清华附中','清华大学'],adddress={'home':'北京','company':'北京小米'},hobby={'打篮球'},province=('狼'),city=None,):  
    print(f"{greeting}, {name}!")  
# 调用函数，只提供必需的参数  
greet("Alice")  
# 输出: Hello, Alice!  
# 调用函数，提供所有参数  
greet("Bob", "Hi")  
# 输出: Hi, Bob!  
# 注释: 在这个例子中，"greeting" 参数有一个默认值 "Hello"。因此，在调用 greet("Alice") 时，  
# Python 会自动将 "greeting" 的值设置为 "Hello"。

#创建携带默认值懒加载
def add_item(item, my_list=None):  
    if my_list is None:  
        my_list = []  
    my_list.append(item)  
    return my_list  

print(add_item(1))  # 输出: [1]  
print(add_item(2))  # 输出: [2]
# 1. 位置参数不能跟在默认参数之后：在函数定义中，所有默认参数都必须位于非默认参数（即必需参数）之后。这是因为Python在调用函数时，首先会匹配位置参数，然后再处理关键字参数。如果默认参数位于非默认参数之前，那么Python将无法确定哪些参数是必需的，哪些参数有默认值。
# 2. 调用时可以使用关键字参数覆盖默认值：在调用函数时，你可以通过关键字参数来覆盖默认参数的值。这是非常有用的，因为它允许你只为需要修改的参数提供值，而保留其他参数的默认值。
# 3. 默认值必须是静态的：如前所述，默认参数的值必须在函数定义时就已经确定，不能是变量。这是因为Python在函数定义时就会计算默认参数的值，并将其存储在函数的 __ defaults __ 属性中。如果默认参数是一个变量，那么该变量在函数定义时的值可能会被后续的代码更改，从而导致不可预测的行为。