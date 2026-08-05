
import time
import functools
#装饰器是高阶函数 + 闭包的语法应用；接收一个可调用对象（函数 / 类），返回新的可调用对象。
# 不修改原函数源码、不改变调用方式，给原函数增加额外功能，遵循开闭原则。
#1.无参通用装饰器（生产标准模板）
def time_cost(func):
    """计时装饰器：统计函数执行耗时"""
    # 复制原函数元信息(__name__、__doc__等)，解决装饰后元信息丢失问题
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """包装函数：承接任意参数，前后插入扩展逻辑"""
        # ========= 函数执行前：前置扩展逻辑 =========
        start = time.time()

        # 透传全部位置参数、关键字参数，调用原始函数，捕获返回值
        ret = func(*args, **kwargs)

        # ========= 函数执行后：后置扩展逻辑 =========
        end = time.time()
        print(f"执行耗时：{end-start:.4f}s")

        # 必须把原函数返回值返回，否则调用方拿到None
        return ret
    return wrapper
# 使用装饰器
@time_cost
def calc(x, y):
    return x ** y
# 调用方式和未装饰完全一致
res = calc(10, 5)
print(res)


#带参数装饰器模板（双层嵌套）
# 分层职责：
# 第一层：接收装饰器自定义配置参数；
# 第二层：真正的装饰器，接收被装饰函数；
# 最内层 wrapper：包装逻辑，处理参数、执行前后扩展。
import time
import functools
def time_cost_with_tip(tip_msg: str):
    """第一层：接收装饰器自定义参数tip_msg"""
    def decorator(func):
        """第二层：真正装饰器，接收被装饰函数"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """最内层包装函数，闭包可以访问tip_msg变量"""
            print(f"[{tip_msg}]开始执行")
            s = time.time()
            res = func(*args, **kwargs)
            e = time.time()
            print(f"[{tip_msg}]结束，耗时{e-s:.4f}")
            return res
        return wrapper
    return decorator
# 使用：传入装饰器自身参数
@time_cost_with_tip(tip_msg="幂运算任务")
def calc(x, y):
    return x ** y
calc(2, 10)