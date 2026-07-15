import traceback
# 完整结构模板
# try:
#     # 【必须】可能出错的代码
#     pass
# except 错误类型1:
#     # 捕获对应异常后的处理
#     pass
# except 错误类型2 as e:
#     # 捕获异常并接收异常信息
#     pass
# else:
#     # 【可选】无异常时执行
#     pass
# finally:
#     # 【可选】无论是否报错，最终一定执行（常用于关闭资源）
#     pass
# 1. try：代码正常执行，无报错则走 else，有报错立即跳转到 except
# 2. except：仅报错时执行，可捕获指定/所有异常
# 3. else：try无任何异常才执行，有异常绝对不执行
# 4. finally：无论成功/失败/return/break，一定会执行
try:
    a = 1
    b = 0
    result = a / b
    print("结果:", result)
except ZeroDivisionError as e:
    # traceback.print_exc()  # 打印报错行数、代码位置、完整链路
    # 保存堆栈到字符串（用于日志存储）
    print(traceback.print_exc())
    err_msg = traceback.format_exc()
    print("打印"+err_msg)


