row = input("input count of rows \
>>> ")
column = input("input count of columns \
>>> ")

if row.isdigit() and column.isdigit():
    row = int(row)
    column = int(column)
    i = 0
    while i < row:
        j = 0
        while j < column:
            if i == 0 or i == row - 1:
                print("*", end='')
            elif (j == 0 or j == column - 1):
                print("*", end='')
            else:
                print(" ", end='')
            j += 1
        i += 1
        print()
else:
    print("Error")