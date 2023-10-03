"""
如果类中的一个方法：
1. 既不访问实例属性或者调用实例方法
2. 也不访问类属性或者调用类方法
此时可以把它封装成一个静态方法
"""

class Dog:
    @staticmethod
    def run():
        print("跑")


Dog.run()