a = {1: "i", "s": 2, (1, 2): 3, None: 4, True: 5, "": 6, -3: 7}
b = {-3: 7, "": 6, None: 4, (1, 2): 3, 1: 5, "s": 2}
print(a == b)
print(a)
print(b)
c = {None: 4, "s": 2, (1, 2): 3, -3: 7, "": 6, 1: 6}
print(a == c)
