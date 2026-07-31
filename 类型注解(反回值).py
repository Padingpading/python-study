from typing import Any

#1.无返回值
def no_resp(msg: str) -> None:
    print("日志：", msg)

def resp_int(a: int, b: int) -> int:
    return a + b

def resp_float() -> float:
    return 0.85

# def get_name() -&gt; str:
#     return "Python注解"

#2.复合类型返回值
# 返回列表
def get_id_list() -> list[int]:
    return [1, 2, 3]

# 返回字典
def get_user_dict() -> dict[str, int]:
    return {"age": 20, "score": 90}

# 返回元组
def get_pos() -> tuple[int, int]:
    return (100, 200)

#3.可选返回值（可能返回 None）
# 写法1：Python3.10+
def find_user(uid: int) -> str | None:
    return "张三" if uid == 1 else None
#4.多类型联合返回值
# 返回 int / str 两种类型
def get_result(flag: bool) -> int | str:
    return 100 if flag else "未知"

#5返回任意类型
def get_random_data() -> Any:
    return [1, 2] or {"name": "test"}