t = ([0], [1])
try:
    t[True] += [5]
except Exception as e:
    print("TE")
try:
    t[-1] += [9]
except Exception as e:
    print("TE2")
try:
    t[-2] *= 2
except Exception as e:
    print("TE3")
print(t)
