xs = [1, 2, 3]
def p(v):
    print(v)
    return v
try:
    print(xs[p(1) // 0])
except Exception as e:
    print("a")
try:
    xs[p(0)] = p(5) // 0
except Exception as e:
    print("b")
print(xs)
d = {}
try:
    d[p(1) // 0] = p(2)
except Exception as e:
    print("c")
print(d)
try:
    xs[p(2)] += p(3) % 0
except Exception as e:
    print("d")
print(xs)
