def p(v):
    print("rhs")
    return v
xs = [1, 2]
try:
    xs[2] += p(1)
except Exception as e:
    print("IE")
try:
    xs[-3] += p(1)
except Exception as e:
    print("IE2")
xs[-2] += p(5)
print(xs)
d = {"a": 1}
try:
    d["b"] += p(1)
except Exception as e:
    print("KE")
print(d)
