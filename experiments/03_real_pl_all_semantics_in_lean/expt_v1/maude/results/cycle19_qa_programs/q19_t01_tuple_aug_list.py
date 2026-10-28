inner = [1]
t = (inner, 2)
try:
    t[0] += [2]
except Exception as e:
    print("TE")
print(inner)
print(t)
try:
    t[0] += (3,)
except Exception as e:
    print("TE2")
print(t)
