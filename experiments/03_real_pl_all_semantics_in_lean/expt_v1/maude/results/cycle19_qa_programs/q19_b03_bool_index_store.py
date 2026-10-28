xs = [0, 0, 0]
xs[True] = 9
xs[False] += 4
xs[True] += 1
print(xs)
t = (1, 2)
try:
    t[True] = 5
except Exception as e:
    print("TE")
try:
    t[True] += 5
except Exception as e:
    print("TE2")
print(t)
