def perfectnum(num):
    sum = 0
    temp = num
    for i in range(1, temp // 2 + 1):
        if temp % i == 0:
            sum += i
    return sum == num

count = 0
i = 10000
while i:
    if perfectnum(i):
        print(i)
        count += 1
    if count == 4:
        break
    i -= 1
else:
    print("count is less than 4")
