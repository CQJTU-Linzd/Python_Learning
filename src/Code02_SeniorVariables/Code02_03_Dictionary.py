# 字典
person = {
    "name": "张三",
    "age": 18,
    "sex": "男"
}
print(person)

# 取值
print(person["name"])

# 增加、修改
person["id"] = 401
person["age"] = 20
print(person)

# 删除
person.pop("sex")
print(person)

# 统计键值对数量
print(len(person))

# 合并字典
tmp = {
    "height": 180
}
person.update(tmp)
print(person)

# 循环遍历
# key是每一对键值对的键值
for key in person:
    print("%s: %s" % (key, person[key]))



