# 找出100~999之间的所有水仙花数
# 水仙花数是各位立方和等于这个数本身的数

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if low ** 3 + mid ** 3 + high ** 3 == num:
        print(num)
