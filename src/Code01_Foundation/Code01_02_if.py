age = input("请输入年龄：")
age = int(age)
if age >= 18:
    print("可以进入！")
else:
    print("不可入内！")


# 逻辑运算 and or not
# 要求age在0-120之间
if 0 <= age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")


# 要求a和b有一个大于60就通过
a = 90
b = 66
if a > 60 or b > 60:
    print("通过")
else:
    print("不通过")


# 非公司人员不得入内
isEmployee = True
if not isEmployee:
    print("非本公司员工，不得入内！")


# elif
holidayName = "情人节"
if holidayName == "情人节":
    print("买玫瑰")
elif holidayName == "平安夜":
    print("吃苹果")
elif holidayName == "生日":
    print("买蛋糕")
else:
    print("每天都是节日")


# if嵌套
hasTicket = True
knifeLength = 30
if hasTicket:
    print("车票检查通过，准备开始安检")
    if knifeLength >= 30:
        print("刀的长度：%d cm，太长，不能上车" % knifeLength)
    else:
        print("安检通过")
else:
    print("车票检查失败")