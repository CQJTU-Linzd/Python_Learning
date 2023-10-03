def inputPassword():
    pwd = input("请输入密码：")
    if len(pwd) >= 8:
        return pwd
    else:
        # 主动抛出异常
        ex = Exception("密码长度不够！")
        raise ex


try:
    inputPassword()
except Exception as res:
    print(res)

