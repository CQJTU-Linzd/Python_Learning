import cardsTools

while True:
    cardsTools.showMenu()
    select = input("请选择要进行的功能：")
    if select in ["1", "2", "3"]:
        if select == "1":
            cardsTools.createCard()
        elif select == "2":
            cardsTools.showCards()
        else:
            cardsTools.queryCard()
    elif select == "0":
        print("欢迎下次使用！")
        break
    else:
        print("输入有误，请重新选择！")


