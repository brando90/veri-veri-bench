# out-of-range index and missing dict key raise catchable exceptions
xs = [10, 20, 30]
t = (1, 2)
s = "abc"
d = {1: 5, 2: 6}
for i in [0, 2, 3, 100, -1, -3, -4, -100]:
    try:
        print(xs[i])
    except Exception as e:
        print(-1)
for i in [1, 2, -2, -3]:
    try:
        print(t[i])
    except Exception as e:
        print(-2)
for i in [0, 3, -1, -4]:
    try:
        print(len(s[i]))
    except Exception as e:
        print(-3)
for k in [1, 2, 3, 0, -1]:
    try:
        print(d[k])
    except Exception as e:
        print(-4)
d2 = {"a": 1}
try:
    d2["b"] += 1
except Exception as e:
    print(len(d2))
print(d2["a"])
ys = [1, 2]
try:
    ys[5] += 1
except Exception as e:
    print(len(ys))
try:
    ys[2] = 9
except Exception as e:
    print(-5)
try:
    ys[-3] = 9
except Exception as e:
    print(-6)
ys[1] = 7
ys[-2] = 6
print(ys[0] + ys[1])
try:
    print(xs[5] + 1)
except Exception as e:
    print(-7)
def g(q):
    return q[9]
try:
    g([1])
except Exception as e:
    print(-8)
e1 = []
try:
    print(e1[0])
except Exception as e:
    print(-9)
try:
    print({}[0])
except Exception as e:
    print(-10)
# an item that is None is still present
n = {1: 5}
n[2] = n[1] * 0
print(n[2])
