# #现有业务函数 calc()，实现计算逻辑。现在需求：在不修改 calc() 函数内部代码的前提下，新增功能：统计函数执行耗时。
import time 

# #方式 1：直接修改原函数（不推荐，侵入式）改动业务函数本体，如果几十个函数都要计时，就要复制粘贴大量计时代码，代码重复、维护麻烦，违反开闭原则。
# import time
# def calc(x, y):
#     start = time.time()
#     res = x ** y
#     end = time.time()
#     print(f"耗时:{end-start:.4f}")
#     return res
# #方式2:调用时手动包裹（可行，但调用处每一处都要改）
# #不用改函数内部，但1.装饰器引入.py是每一次调用都要写计时逻辑，调用点多就会到处重复代码。

def add(x,y):
    return x+y
start =  time.time()
result =  add(10,5)
end = time.time()
# 打印耗时
print(f"耗时:{end-start}")


