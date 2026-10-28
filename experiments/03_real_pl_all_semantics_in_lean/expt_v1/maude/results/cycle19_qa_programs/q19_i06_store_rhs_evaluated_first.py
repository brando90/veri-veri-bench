def p(v):
    print("rhs")
    return v
xs = [1, 2]
try:
    xs[5] = p(9)
except Exception as e:
    print("IE")
print(xs)
t = (1, 2)
try:
    t[0] = p(3)
except Exception as e:
    print("TE")
print(t)
