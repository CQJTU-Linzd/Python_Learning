# 捕获未知错误
try:
    num = int(input("请输入一个整数："))
    res = 8 / num
    print(res)
except Exception as result:
    print("发生错误：%s" % result)








