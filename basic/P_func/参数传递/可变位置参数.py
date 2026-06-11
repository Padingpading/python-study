#可变位置参数
# 在Python中，可变位置参数（通常表示为*args）是一种允许你将不定数量的参数传递给函数的机制。
# 这里的“可变”指的是传递给函数的参数数量不是固定的，而是由调用者决定的。
# *args在函数定义中作为参数列表的最后一个元素出现，它接收一个元组，
# 该元组包含了所有传递给函数但未被前面定义的参数名捕获的额外位置参数。


#定义
# def function_name(*args):  
#     # 函数体，args是一个元组，包含了所有额外的位置参数  
#     pass

# 定义函数，使用*args接收可变数量的位置参数  
def greet(*names):  
    print(type(names))#tuple
    for name in names:  
        print(f"Hello, {name}!")  
# 调用函数，传递多个参数  
greet("Eve", "Frank", "Grace")  
# 输出:  
# Hello, Eve!  
# Hello, Frank!  
# Hello, Grace!  
# 注释: *names会将多个参数接收为元组names，然后在函数体内遍历

#注意点
#1.*args 必须写在普通位置参数后面：前面有名参数先按顺序接住，剩下的才进 *args。
#  正确写法：
def order_total(price, count='countdf', *extras):
    # price、count 先被匹配，extras 收到多出来的位置参数（元组）
    print(f"单价={price}, 数量={count}, 额外费用={extras}")
    return price * count + sum(extras)  

order_total(10, 2,'name')              # 单价=10, 数量=2, 额外费用=()
order_total(10, 2, 5, 3)        # 单价=10, 数量=2, 额外费用=(5, 3)
print(order_total(10, 2, 5, 3)) # 28

#  错误写法（语法错误，不能运行）：
# def bad(*args, price):   # SyntaxError: *args 后面不能再跟普通位置参数
#     pass
#2.与关键字参数的组合：args可以与关键字参数一起使用，但关键字参数必须位于 *args之后（如果函数还定义了其他非默认参数，则这些参数也必须位于·* args之前）。此外，还可以有一个特殊的**kwargs参数（可变关键字参数），它位于* args之后，用于接收任意数量的关键字参数。

#3.参数解包：在调用函数时，可以使用*操作符将列表、元组或其他可迭代对象解包为位置参数。这允许你将存储在容器中的数据作为单独的参数传递给函数。
def sum_numbers(*args):  
    return sum(args)  
numbers = [1, 2, 3, 4]  
print(sum_numbers(*numbers))  # 输出: 10