"""
测试场景：随便一个方法加上 @time_cost 会怎么样
结论：调用方式不变、返回值不变，只是每次调用多一层计时逻辑。
"""
import functools
import time


def time_cost(func):
    """无参通用装饰器"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(f"[time_cost] {func.__name__} 耗时：{end - start:.4f}s")
        return ret
    return wrapper


# ---------- 场景1：无参函数 ----------
@time_cost
def hello():
    """打招呼"""
    print("hello")
    return "ok"


# ---------- 场景2：位置参数 ----------
@time_cost
def add(a, b):
    return a + b


# ---------- 场景3：关键字参数 / 默认参数 ----------
@time_cost
def greet(name, msg="你好"):
    return f"{msg}, {name}"


# ---------- 场景4：可变参数 ----------
@time_cost
def total(*nums, **options):
    base = sum(nums)
    if options.get("double"):
        base *= 2
    return base


# ---------- 场景5：类里的各种方法 ----------
class Demo:
    @time_cost
    def instance_method(self, x):
        return x * 2

    @classmethod
    @time_cost
    def class_method(cls, x):
        return f"{cls.__name__}:{x}"

    @staticmethod
    @time_cost
    def static_method(x):
        return x + 1


# ---------- 场景6：验证 wraps 保留元信息 ----------
def check_wraps():
    print("函数名:", hello.__name__)      # 期望: hello（不是 wrapper）
    print("文档字符串:", hello.__doc__)  # 期望: 打招呼


if __name__ == "__main__":
    print("===== 1. 无参函数 =====")
    print("返回值:", hello())

    print("\n===== 2. 位置参数 =====")
    print("返回值:", add(3, 5))

    print("\n===== 3. 关键字 / 默认参数 =====")
    print("返回值:", greet("小明"))
    print("返回值:", greet(name="小红", msg="早上好"))

    print("\n===== 4. *args / **kwargs =====")
    print("返回值:", total(1, 2, 3, double=True))

    print("\n===== 5. 类方法 =====")
    demo = Demo()
    print("实例方法:", demo.instance_method(10))
    print("类方法:", Demo.class_method(20))
    print("静态方法:", Demo.static_method(30))

    print("\n===== 6. wraps 元信息 =====")
    check_wraps()

    print("\n结论：任意方法加上规范的 @time_cost，都能正常调用，只是多了耗时打印。")
