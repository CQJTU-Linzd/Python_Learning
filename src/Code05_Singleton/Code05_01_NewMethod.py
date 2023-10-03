"""
__new__方法
创建对象时，new方法会被自动调用
1. 在内存中为对象分配空间
2. 返回对象的引用
"""
class MusicPlayer(object):
    def __init__(self):
        print("播放器初始化")
    def __new__(cls, *args, **kwargs):
        print("new方法调用")
        return super().__new__(cls) # 必须返回这句


mp = MusicPlayer()
print(mp)