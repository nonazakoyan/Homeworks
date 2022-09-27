def ft_isdigit(number):
    if number.isdigit() or (number[0] == "-" and number[1:].isdigit()):
        return True
    return False

first = input("input the first number: \
>>> ")
second = input("input the second number: \
>>> ")

if ft_isdigit(first) and ft_isdigit(second):
    first = int(first)
    second = int(second)
    try:
        res = abs(first - second) / (first + second)
        print(f'{res:.2f}')

    except ZeroDivisionError:
        print("division by zero: ")
else:
    print("invalid input: ")
