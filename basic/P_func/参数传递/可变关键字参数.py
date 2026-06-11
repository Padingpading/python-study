#可以使用可变关键字参数。**kwargs会将接收到的多个关键字参数值作为字典（dict）传递。 
#在Python中，**kwargs（关键字参数）是一种在函数定义时使用的特殊语法，它允许你将不定长度的关键字参数传递给一个函数#
#。这些关键字参数在函数内部被收集到一个名为kwargs（虽然你可以使用任何变量名，但kwargs是约定俗成的）的字典中。
#这使得函数能够处理比预先定义更多的参数，增加了函数的灵活性和通用性。 

#定义
def greet(**kwargs):  
    for key, value in kwargs.items():  
        print(f"{key}: {value}")  
#使用关键字传参
greet(name="Alice", age=30, country="Wonderland")
# 注释: **kwargs会将多个关键字参数接收为字典kwargs，然后可以通过items()遍历

# 1. 命名冲突：虽然你可以使用任何变量名来代替kwargs，但最好遵循约定使用kwargs，以避免与其他变量名冲突或造成混淆。

# 2. 参数顺序：定义时固定参数 → *args → **kwargs，*args 必须在 **kwargs 前面。
#  正确写法（完整顺序）
def create_user(name, age, *hobbies, **profile):
    # name、age：固定位置参数（先匹配）
    # hobbies：多出来的位置参数 → 元组
    # profile：多出来的关键字参数 → 字典
    print(f"姓名={name}, 年龄={age}")
    print(f"爱好={hobbies}")
    print(f"档案={profile}")
create_user("张三", 18, "篮球", "游泳", city="北京", phone="12345")
# 姓名=张三, 年龄=18
# 爱好=('篮球', '游泳')
# 档案={'city': '北京', 'phone': '12345'}

#  记忆口诀：先位置，后关键字；先 *args，后 **kwargs
#  def 函数(普通参数, *args, 仅关键字参数=默认值, **kwargs)
#  错误写法（语法错误，不能运行）：
# def bad(**kwargs, *args):   # SyntaxError: *args 不能写在 **kwargs 后面
#     pass
# def bad2(**kwargs, name):   # SyntaxError: 普通参数不能写在 **kwargs 后面
#     pass

# 3. 默认值：**kwargs 是字典，调用时没传的关键字不会出现在字典里，所以不能像普通参数那样直接写默认值。
# def show(**kwargs, city="北京"):   # SyntaxError: **kwargs 后面不能再写普通参数
# def show(**kwargs="默认值"):       # SyntaxError: 不能给 **kwargs 本身赋默认值
#  kwargs 没收到参数时就是空字典，不会自动带上默认值

# 4. 修改kwargs：虽然你可以在函数内部修改kwargs字典，但这通常不是一个好主意，因为它可能会影响到函数外部的状态，导致代码难以理解和维护。
# 5. 用途：kwargs非常适合于那些需要高度灵活性的函数，特别是当你不知道函数将接收哪些关键字参数时。然而，过度使用kwargs可能会使函数签名变得模糊，降低代码的可读性和可维护性。因此，在可能的情况下，最好明确指定函数所需的参数。

