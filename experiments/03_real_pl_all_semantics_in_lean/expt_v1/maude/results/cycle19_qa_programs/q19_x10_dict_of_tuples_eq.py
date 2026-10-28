a = {"p": (1, {2: 3, 4: 5}), "q": [True, (None,)]}
b = {"q": [1, (None,)], "p": (True, {4: 5, 2: 3})}
print(a == b)
print(a != b)
