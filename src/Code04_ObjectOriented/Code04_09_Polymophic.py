class Dog(object):
    def __init__(self, name):
        self.name = name
    def game(self):
        print("%s在地上玩耍" % self.name)


class XiaoTianDog(Dog):
    def game(self):
        print("%s在天上玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name
    def gameWithDog(self, dog):
        print("%s和%s一起玩耍" % (self.name, dog.name))
        dog.game()


dog = Dog("旺财")
p = Person("小明")
p.gameWithDog(dog)
dog2 = XiaoTianDog("哮天犬")
p.gameWithDog(dog2)