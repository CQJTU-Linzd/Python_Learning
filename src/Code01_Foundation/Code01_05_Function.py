def multipleTable(): # 函数定义
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

multipleTable()

# 函数参数的使用
def twoSum(num1, num2):
    print("%d + %d = %d" % (num1, num2, num1 + num2))
    num1 -= 10
    num2 -= 10

num1 = 5
num2 = 10
twoSum(5, 10)
print("num1 = %d  num2 = %d" % (num1, num2)) # 5  10