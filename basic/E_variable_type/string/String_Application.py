s = "job , alice , jack , leo"
s_list = s.split(",")
for item in s_list:
    # 去除前后的空格
    print(item.strip())
