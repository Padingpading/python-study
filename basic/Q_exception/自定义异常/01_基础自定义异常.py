# 自定义业务异常
class BusinessError(Exception):
    pass
# 使用
def login(pwd):
    if pwd != "123456":
        raise BusinessError("密码错误")
try:
    login("111")
except BusinessError as e:
    print("业务报错：", e)