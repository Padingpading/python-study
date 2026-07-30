# 格式
# def 函数名(参数1: 类型1, 参数2: 类型2 = 默认值) -> 返回值类型:
#     函数逻辑

#基础类型入参（int / float / str / bool）
# 入参约束：整型、浮点型、字符串、布尔值
def user_info(age: int, height: float, name: str, is_vip: bool) -> None:
    print(name, age, height, is_vip)

#带默认值入参
def show_tip(tip: str = "操作成功") -> None:
    print(tip)

#复合类型入参（list / dict / tuple / set）
# 列表、字典、元组、集合 入参注解
def data_handle(nums: list[int], info: dict[str, str], pos: tuple[int,str], tags: set[str]) -> None:
    print(nums, info, pos, tags)
data_handle(nums=[1,2,3], info={"name":"张三"}, pos=(1,"123"), tags={"1","2","3"})
