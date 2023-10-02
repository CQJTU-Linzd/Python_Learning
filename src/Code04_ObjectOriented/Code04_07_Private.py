class Girl:
    def __init__(self, name):
        self.name = name
        self.__age = 18 # 私有属性
    def secret(self):
        print("我的年龄是：%d" % self.__age)

g = Girl("小芳")
g.secret()