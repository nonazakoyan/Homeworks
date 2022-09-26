def ft_isdigit(number):
    if number.isdigit() or (number[0] == "-" and number[1:].isdigit()):
        return True
    return False

number = input("input the number: \
>>> ").strip()

if ft_isdigit(number):
    sum = 0
    number = abs(int(number))
    while int(number):
        sum += number % 10
        number //= 10
    print(sum)
else:
    print("input is wrong! ")
