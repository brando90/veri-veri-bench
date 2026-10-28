xs = [(1,), [2]]
u = xs[0]
try:
    u[0] = 3
except Exception as e:
    print("TE")
v = xs[1]
v[0] = 3
print(xs)
