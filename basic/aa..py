from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 启动Chromium浏览器内核
    # headless=False：显示可视化浏览器窗口（调试专用）
    # slow_mo=500：所有操作延迟500毫秒执行，放慢速度，方便观察流程、调试报错
    browser = p.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
    proxy = {
        "server": "http://223.93.69.252:47890",
        "username": "ripw0708fx1002",
        "password": "GrJ_20260708",
        # 跳过使用代理
        "bypass": "localhost,127.0.0.1"
    }

    #
dict = {"my_key": "my_value"}
context = browser.new_context(
    viewport=None,
    proxy=proxy,
    dict={"my_key": "my_value"}
)

page = context.new_page();

# 跳转指定网址，自动等待页面DOM、网络加载完成
page.goto("https://test-tsc.wanmashijie.com/recommendSource/index")

is_dark = page.evaluate("window.matchMedia('(prefers-color-scheme: dark)').matches")
print(is_dark)
# 获取并打印当前页面标题，校验页面是否正常加载
print("当前页面标题：", page.title())
# 定位元素
# 关闭浏览器，释放所有资源
sleep(50)
browser.close()
