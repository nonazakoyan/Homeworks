from curses.ascii import isdigit


weight = input("input the weight in kilograms: \
>>> ").strip()

if weight.isdigit():
    print(f'{(int(weight) * 2.2):.2f}')
else:
    print("input is negative or invalid number: ")
