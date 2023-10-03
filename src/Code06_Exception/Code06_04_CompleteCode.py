try:
    num = int(input("请输入一个整数："))
    res = 8 / num
    print(res)
except ZeroDivisionError:
    print("除0错误！")
except ValueError:
    print("值错误！")
except Exception as result:
    print("发生错误：%s" % result)
else: # 没有出现异常，成功尝试，才会执行的代码
    print("尝试成功！")
finally:
    print("无论是否出现错误，都会执行")