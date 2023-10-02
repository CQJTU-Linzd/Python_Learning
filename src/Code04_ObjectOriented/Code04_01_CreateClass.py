class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)
    def drink(self):
        print("%s爱喝水" % self.name)

# 创建猫对象
cat = Cat()

# 类外给对象增加属性：不推荐
cat.name = "Tom"
print(cat.name)

cat.eat()
cat.drink()