class ApiError(Exception):
    """接口统一异常"""
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return f"【{self.code}】{self.msg}"
# 抛出
raise ApiError(500, "服务器接口请求失败")