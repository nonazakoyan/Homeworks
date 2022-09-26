num = input("input the n-th fibonacci number \
>>> ")

if num.isdigit():
    first = 0
    second = 1
    next = 0
    i = 1
    while i < int(num):
        first, second = second, next
        next = first + second
        i += 1
    print(next)
else:
    print("input is wrong! ")
