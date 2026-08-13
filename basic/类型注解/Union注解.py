from typing import Union

Union[int, str]

#Python3.9+ 简化管道符写法（推荐）
int | str



#函数参数注解
 # 3.9+ 原生写法
def get_info(data: int | float) -> float:
    return float(data)
# 3.8及以下兼容写法
def get_info(data: Union[int, float]) -> float:
    return float(data)

#2. 变量注解
# 单个变量支持两种类型
val: str | None = None
val = "测试文本"


#返回值多类型标注
from typing import Union
def find_user() -> Union[dict, None]:
    """找到用户返回字典，无数据返回None"""
    return None
#嵌套 Union（多类型组合）
# 支持 int / str / None
num: int | str | None = 6.66


# Union 核心特点
# 或关系：变量满足其中任意一种类型即合法，不是同时满足；
# 扁平化自动合并：Union[int, Union[str, None]]等价于int | str | None，无需手动嵌套；
# 可与容器类型组合：list[int | str] 列表内元素支持数字或字符串；
# 兼容静态检查工具：mypy、pyright、pycharm 全部识别；
# None专用简写：Optional[T] = Union[T, None]，二者完全等价。