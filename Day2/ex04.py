year = input("input the year: \
>>> ").strip()

def LeapYear(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return 0

def NextLeapYear(year):
    while True:
        if LeapYear(year):
            return year
        year += 1

if year.isdigit() and int(year) > 1600:
    FstLeap = NextLeapYear(1600)
    count = 0
    for i in range(FstLeap, int(year), 4):
        count += 1
    print(count)  
else:
    print("invalid input or less than 1600: ")  
