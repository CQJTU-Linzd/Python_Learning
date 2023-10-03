class Tool:
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1

    # 类方法 显示工具计数
    @classmethod
    def showCount(cls):
        print("工具对象的数量：%d" % cls.count)


t1 = Tool("斧头")
t2 = Tool("榔头")
t3 = Tool("锯子")
Tool.showCount()