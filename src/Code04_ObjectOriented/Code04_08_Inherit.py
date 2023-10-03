class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")

# 继承语法
class Dog(Animal):
    def bark(self):
        print("汪汪叫")
        # 子类中调用父类方法
        super().run()


dog = Dog()
dog.eat()
dog.drink()
dog.run()
dog.bark()