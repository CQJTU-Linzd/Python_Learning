print("Hello World" + "!!!")

print(
    '''
name: 张三
    age: 18
    id: 001
    
    '''
)

# 不想换行
print("***", end = "")

# 输入
a = input("请输入密码：")
print(a)

# 转成int类型
b = int(a)
print(type(b))

# 转成float类型
c = "3.14"
c = float(c)
print(type(c))

# 格式化输出
age = 18
name = "小明"
print("年龄：%d" % age)
print("姓名：%s 年龄：%d" % (name, age))
