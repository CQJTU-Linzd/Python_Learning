str = "hello world"
print(str[3])
for ch in str:
    print(ch)

# 长度
print(len(str))

# 统计某一个子串出现次数
print(str.count("l"))

# 某个子串出现的位置
print(str.index("o"))

# 去除空白字符
str = "    asdasd   "
# 去掉左边空白字符
print(str.lstrip())
# 去掉右边空白字符
print(str.rstrip())
# 去掉两边空白字符
print(str.strip())


# 拆分字符串
str = "a,b,cd,e"
strList = str.split(",")
print(strList)

# 合并字符串
joinStr = " ".join(strList)
print(joinStr)


# 字符串切片
str = "abcdefghi"
# [开始索引:结束索引:步长]
# 左闭右开
substr = str[0:len(str):2]
print(substr)

# 索引值为-1表示从字符串的最后一个字符
# 步长为-1表示从右向左跳
revStr = str[-1::-1]
print(revStr)
