class Cat:
    def __init__(self, name):
        print("这是一个初始化方法")
        self.name = name
    def eat(self):
        print("%s爱吃鱼" % self.name)

    # __str__ 方法重载print函数，能够自定义打印对象的内容
    # 该方法必须返回字符串
    def __str__(self):
        return "我是小猫" + self.name

cat = Cat("Tom")
print(cat)