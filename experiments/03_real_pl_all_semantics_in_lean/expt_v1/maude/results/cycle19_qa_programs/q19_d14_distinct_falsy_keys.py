a = {None: 1, 0: 2, "": 3, (): 4}
b = {(): 4, "": 3, 0: 2, None: 1}
print(a == b)
print(len(a))
c = {(): 4, "": 3, False: 2, None: 1}
print(a == c)
