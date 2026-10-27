xs = [1]
xs += (2, 3)
ys = xs + [4]
print(ys)
t = (1,) + (2,)
t2 = t * 2 + t
print(t2)
print(len(t2))
