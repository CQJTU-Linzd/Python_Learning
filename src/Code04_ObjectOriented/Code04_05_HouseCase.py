# 摆放家具
# 家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s，占地：%.2f]" % (self.name, self.area)

# items = []
# items.append(HouseItem("席梦思", 4))
# items.append(HouseItem("衣柜", 2))
# items.append(HouseItem("餐桌", 3))
#
# print(items)
#
# for it in items:
#     print(it)

# 房子类
class House:
    def __init__(self, houseType, area):
        self.houseType = houseType
        self.area = area
        self.restArea = area
        self.items = []
    def __str__(self):
        return ("户型：%s 占地面积：%.2f 剩余面积：%.2f 家具列表：%s"
                % (self.houseType, self.area, self.restArea, self.items))
    def addItem(self, item):
        if self.restArea < item.area:
            print("房子剩余面积不足！无法添加！")
        else:
            self.restArea -= item.area
            self.items.append(item.name)
            print("家具：%s[占地面积：%.2f] 添加成功！" % (item.name, item.area))

# 创建房子对象
house = House("两室一厅", 15)
print(house)


items = []
items.append(HouseItem("席梦思", 4))
items.append(HouseItem("衣柜", 2))
items.append(HouseItem("餐桌", 3))

for it in items:
    house.addItem(it)

print(house)






