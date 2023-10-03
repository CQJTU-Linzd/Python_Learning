"""
类属性就是给类对象中定义的属性
通常用来记录与这个类相关的特征
不会用于记录具体对象的特征
"""

# 需求：想知道当前这个类，创建了多少个对象
class Tool:
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1


t1 = Tool("斧头")
t2 = Tool("榔头")
t3 = Tool("锯子")
print(Tool.count) # 不推荐

