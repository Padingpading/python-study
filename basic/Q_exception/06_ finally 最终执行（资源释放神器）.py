f = None
try:
    f = open("test.txt", "r", encoding="utf-8")
    print(f.read())
except Exception as e:
    print("文件读取失败：", e)
finally:
    # 无论成功失败，都关闭文件，防止资源泄露
    if f:
        f.close()
    print("文件资源已释放")