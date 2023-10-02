class Cat:
    def __init__(self, name):
        print("这是一个初始化方法")
        self.name = name
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("这是析构函数")


cat = Cat("Tom")
cat.eat()