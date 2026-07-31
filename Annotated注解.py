from typing import Annotated, get_args
from typing import Annotated
from pydantic import Field
# 标准语法
# Annotated[原始类型, 附加信息1, 附加信息2, ...]
# - 第一个参数：原始基础类型（int/str/list/自定义类型）
# - 后续参数：任意数量、任意类型的附加元数据（字符串、数字、校验对象、类、函数均可）

# int类型 + 中文业务说明
# int类型 + 中文业务说明
def get_user_info(
        age: Annotated[int, "用户年龄，范围0-120"],
        username: Annotated[str, "用户登录账号，非空"]
) -> None:
    pass
# 进阶用法：附加数值校验规则
# 年龄：int类型，0~120
AgeType = Annotated[int, "用户年龄", 0, 120]
# 密码：字符串，长度6-20位
PwdType = Annotated[str, "登录密码", 6, 20]
def register(age: AgeType, pwd: PwdType) -> None:
    # get_args 取出元数据：类型, 说明, 最小, 最大
    _, _, age_min, age_max = get_args(AgeType)
    _, _, pwd_min, pwd_max = get_args(PwdType)

    if not (age_min <= age <= age_max):
        raise ValueError(f"年龄需在 {age_min}~{age_max}")
    if not (pwd_min <= len(pwd) <= pwd_max):
        raise ValueError(f"密码长度需在 {pwd_min}~{pwd_max}")

    print(f"注册成功: age={age}, pwd={pwd}")

register(18, "abc123")

#搭配第三方校验（FastAPI/Pydantic 核心用法）


# 附加字段规则：最小值1，最大值999，字段描述
UserId = Annotated[int, Field(gt=0, lt=1000, description="用户唯一ID")]
def get_user(uid: UserId) -> None:
    pass

#复合类型增强注解
from typing import Annotated
# 整型列表，存储用户ID
IdList = Annotated[list[int], "用户ID集合，元素均为正整数"]
def batch_get(ids: IdList) -> None:
    pass
