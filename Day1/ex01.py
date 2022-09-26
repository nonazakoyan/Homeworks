def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

def ft_isdigit(number):
    if number.isdigit() or (number[0] == "-" and number[1:].isdigit()):
        return True
    return False

number = input('''Input the number:
>>>  ''')

number = number.strip()
if ft_isdigit(number):
    print(even_or_odd(int(number)))
else:
    print("input isn't number")
