# while
# 打印5遍hello world
i = 0
while i < 5:
    print("hello world")
    i += 1

# 1-100累加和
sum = 0
i = 0
while i <= 100:
    sum += i
    i += 1
print(sum)


i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1

# 九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d\t" % (j, i, i * j), end=" ")
        j += 1
    # print("%d" % i)
    print("")
    i += 1