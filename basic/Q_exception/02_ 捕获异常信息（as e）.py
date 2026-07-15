ZeroDivisionError
try:
    a = 1 / 0
except ZeroDivisionError as e:
    print("异常详情：", e)
    print("异常类型：", type(e))