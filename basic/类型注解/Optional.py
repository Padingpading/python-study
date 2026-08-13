from typing import Optional
# 基础语法
#变l[数据类型]
# 带默认值完整语法
#参数: Optional[数据类型] = None

#1.函数入参注解（最常用）
# token：可以是字符串、可以是None，默认空
def login_optional(token: Optional[str]) -> None:
    print(token)

def login_or(token: str |None ) -> None:
    print(token)

#2.函数返回值注解
def find_username(uid: int) -> Optional[str]:
    if uid == 1:
        return "Python笔记"
    # 查询不到自动返回None，完全匹配注解
    return None

#3.多类型
def test_num(num: Optional[int] = None) -> Optional[float]:
    return 99.9 if num else None

# #Optional 核心特点
# 1. 空值兼容：唯一作用就是让指定类型兼容 None 空值，无其他额外功能。
# 2. 版本兼容强：Python3.5+ 全版本支持，是低版本 Python 实现可空类型的唯一方案。
# 3. 纯标记属性：和所有类型注解一致，仅用于IDE提示、静态校验，不影响代码运行。
# 4. 语法统一：支持所有基础类型、复合类型、自定义类型嵌套使用。
# 5. 可替代升级：Python3.10+ 可直接用 T | None 替代，语法更简洁。

if __name__ == "__main__":
    print("=== 1. 入参 Optional[str] / str | None ===")
    login_optional("abc-token")
    login_optional(None)
    login_or("xyz-token")
    login_or(None)

    print("=== 2. 返回值 Optional[str] ===")
    print(find_username(1))   # Python笔记
    print(find_username(99))  # None

    print("=== 3. 入参默认 None + 返回 Optional[float] ===")
    print(test_num())         # None（默认 num=None，if num 为假）
    print(test_num(0))        # None（0 为假）
    print(test_num(10))       # 99.9