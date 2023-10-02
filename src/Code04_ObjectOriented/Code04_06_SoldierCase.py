import random


# 枪类
class Gun:
    def __init__(self, name, maxBullet):
        self.name = name
        self.maxBullet = maxBullet
        self.restBullet = 0
    def __str__(self):
        return ("枪械名称：%s，载弹量：%d，当前弹夹剩余子弹：%d"
                % (self.name, self.maxBullet, self.restBullet))
    def addBullet(self, num):
        self.restBullet = min(self.maxBullet, self.restBullet + num)
        print("装弹成功！当前弹夹剩余子弹：%d" % self.restBullet)
    def shoot(self):
        if self.restBullet == 0:
            print("弹夹为空，请上弹！")
            return False
        else:
            num = random.randint(1, self.restBullet)
            self.restBullet -= num
            print("发射了%d发子弹，剩余%d发子弹" % (num, self.restBullet))
            return True

gun = Gun("AK47", 30)
gun.addBullet(40)
print(gun)
# gun.shoot()


# 士兵类
class Soldier:
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun
    def __str__(self):
        if self.gun is None:
            return ("士兵：%s 未配备枪！" % self.name)
        else:
            return ("士兵：%s 配备武器：%s" % (self.name, self.gun.name))
    def fire(self):
        if self.gun is None:
            print("当前未配备枪，无法开火！")
        else:
            flag = self.gun.shoot()
            if not flag:
                self.gun.addBullet(self.gun.maxBullet)



sold = Soldier("许三多", gun)
print(sold)
sold.fire()














