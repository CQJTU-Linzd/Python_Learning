# 根据错误类型捕获异常
try:
    num = int(input("请输入一个整数："))
    res = 8 / num
    print(res)
except ZeroDivisionError:
    print("除0错误！")
except ValueError:
    print("值错误！")