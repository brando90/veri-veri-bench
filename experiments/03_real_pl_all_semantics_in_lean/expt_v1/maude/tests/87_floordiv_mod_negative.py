# // and % with negative operands follow Python (floor, sign of the divisor)
a = [7, -7, 8, -8, 0, 1]
b = [2, -2, 3, -3, 4, -5, 7, -7, 1, -1]
for x in a:
    for y in b:
        print(x // y)
        print(x % y)
