# 小明跑步
class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return ("我的名字是%s，我的体重是%.2f" % (self.name, self.weight))
    def run(self):
        print("%s爱跑步，跑步可以减轻体重" % self.name)
        self.weight -= 0.5
        self.showWeight()
    def eat(self):
        print("%s是吃货，吃完体重会增加" % self.name)
        self.weight += 1
        self.showWeight()
    def showWeight(self):
        print("%s现在的体重：%.2f" % (self.name, self.weight))

p = Person("小明", 50)
print(p)
p.run()
p.eat()