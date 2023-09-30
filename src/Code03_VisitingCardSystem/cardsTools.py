cardList = []

def showMenu():
    print("*" * 50)
    print("欢迎使用名片管理系统")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("0. 退出系统")
    print("*" * 50)


def createCard():
    name = input("请输入姓名：")
    phone = input("请输入电话号码：")
    qq = input("请输入QQ：")
    email = input("请输入邮箱：")
    cardDict = {
        "name": name,
        "phone": phone,
        "qq": qq,
        "email": email
    }
    cardList.append(cardDict)
    print("名片添加成功！")


def showCards():
    if len(cardList) == 0:
        print("当前没有任何名片记录！")
    else:
        # 打印表头
        for name in ["姓名", "电话", "qq", "邮箱"]:
            print(name, end="\t\t")
        print("")
        print("-" * 50)
        for curCard in cardList:
            print("%s\t\t%s\t\t%s\t\t%s" % (curCard["name"],
                                            curCard["phone"],
                                            curCard["qq"],
                                            curCard["email"]))

def queryCard():
    while True:
        print("1. 按姓名查询")
        print("2. 按电话查询")
        print("0. 退出")
        select = input("请选择查询方式：")

        # 按姓名查询
        if select == "1":
            targetName = input("请输入要查找的姓名：")
            find = False
            index = 1
            findList = []
            for card in cardList:
                if targetName == card["name"]:
                    if not find:
                        # 打印表头
                        for name in ["编号", "姓名", "电话", "qq", "邮箱"]:
                            print(name, end="\t\t")
                        print("")
                        print("-" * 50)
                    find = True
                    print("%d\t\t%s\t\t%s\t\t%s\t\t%s" % (index, card["name"],card["phone"],card["qq"],card["email"]))
                    findList.append(card)
                    index += 1

                    updateCard(findList)
            if not find:
                print("未查询到该名片！")
        # 按电话查询
        elif select == "2":
            targetPhone = input("请输入要查找的电话号码：")
            findList = []
            for card in cardList:
                if targetPhone == card["phone"]:
                    # 打印表头
                    for name in ["编号", "姓名", "电话", "qq", "邮箱"]:
                        print(name, end="\t\t")
                    print("")
                    print("-" * 50)
                    print("%d\t\t%s\t\t%s\t\t%s\t\t%s" % (1, card["name"], card["phone"], card["qq"], card["email"]))

                    findList.append(card)
                    updateCard(findList)

                    break
            else:
                print("未查询到该名片！")


        elif select == "0":
            break

        else:
            print("输入有误，请重新输入！")


def updateCard(findList):
    index = input("请选择要处理的名片编号：")
    if int(index) <= len(findList):
        card = findList[int(index) - 1]
        act = input("请输入对该名片的操作："
                    "[1] 修改  [2] 删除  [0] 返回上级菜单")
        if act == "1":
            while True:
                select = input("请选择要修改的信息："
                               "[1] 姓名 [2] 电话 [3] qq [4]邮箱")
                if select == "1":
                    card["name"] = input("姓名：")
                    break
                elif select == "2":
                    card["phone"] = input("电话：")
                    break
                elif select == "3":
                    card["qq"] = input("qq：")
                    break
                elif select == "4":
                    card["email"] = input("email：")
                    break
                else:
                    print("输入无效！请重新选择")
        elif act == "2":
            cardList.remove(card)
            print("删除成功！")
    else:
        print("编号无效！")