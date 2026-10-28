d1 = {}
d1[1] = [True]
d1[True] = d1[1] + [False]
print(d1)
d2 = {1: [1, 0]}
print(d1 == d2)
