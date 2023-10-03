"""
单例：让类创建的对象，在系统中只有唯一的一个实例
1. 定义一个类属性，初始值是None，用于记录单例对象的引用
2. 重写__new__ 方法
3. 如果类属性 is None，调用父类方法分配空间，并在类属性中记录结果
4. 返回类属性中记录的对象引用
"""
class MusicPlayer(object):
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    # 构造函数还是创建一个对象就调用一次
    def __init__(self):
        print("初始化播放器")


mp1 = MusicPlayer()
print(mp1)
mp2 = MusicPlayer()
print(mp2)