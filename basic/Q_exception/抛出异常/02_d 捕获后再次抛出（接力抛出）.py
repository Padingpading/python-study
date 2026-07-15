try:
    1 / 0
except ZeroDivisionError as e:
    print("捕获到除零错误")
    raise  # 原样向上抛出异常