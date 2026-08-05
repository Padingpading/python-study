# 现有业务函数 calc()，实现计算逻辑。现在需求：在不修改 calc() 函数内部代码的前提下，新增功能：统计函数执行耗时。
import time


# 方式 1：直接修改原函数（不推荐，侵入式）
# 改动业务函数本体，如果几十个函数都要计时，就要复制粘贴大量计时代码，代码重复、维护麻烦，违反开闭原则。
def calc_v1(x, y):
    start = time.time()
    res = x ** y
    end = time.time()
    print(f"[方式1] 耗时:{(end - start) * 1000:.4f} 毫秒, 结果:{res}")
    return res


# 方式2:调用时手动包裹（可行，但调用处每一处都要改）
# 不用改函数内部，但是每一次调用都要写计时逻辑，调用点多就会到处重复代码。
def calc(x, y):
    return x ** y


def add(x, y):
    return x + y


if __name__ == "__main__":
    print("=== 方式1：侵入式改函数本体 ===")
    calc_v1(2, 20)

    print("=== 方式2：调用处手动包裹 ===")
    start = time.time()
    result = calc(2, 20)
    end = time.time()
    print(f"[方式2-calc] 耗时:{(end - start) * 1000:.4f} 毫秒, 结果:{result}")

    start = time.time()
    result = add(10, 5)
    end = time.time()
    print(f"[方式2-add] 耗时:{(end - start) * 1000:.4f} 毫秒, 结果:{result}")

    # 方式2 的痛点：每个调用点都要再写一遍计时
    start = time.time()
    result = add(100, 200)
    end = time.time()
    print(f"[方式2-add再次] 耗时:{(end - start) * 1000:.4f} 毫秒, 结果:{result}")

#方式3 方案 C：手写高阶函数包装（装饰器雏形）
import time
def time_wrapper(func):
    def inner(x, y):
        start = time.time()
        ret = func(x, y)
        end = time.time()
        print(f"耗时:{end-start:.4f}")
        return ret
    return inner

def calc(x, y):
    return x ** y

# 手动完成包装替换
calc = time_wrapper(calc)
res = calc(10, 5)
print(res)