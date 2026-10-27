xs = [10, 20, 30, 40, 50]
for v in xs[1:4]:
    print(v)
ys = xs[:2]
print(len(ys))
print(ys[0] + ys[1])
zs = xs[3:]
print(zs[0])
print(len(xs[:]))
t = (1, 2, 3, 4)
u = t[1:3]
print(u[0] * 10 + u[1])
s = "hello world"
print(len(s[0:5]))
print(len(s[6:]))
print(s[0:5] == "hello")
print(len(xs[-2:]))
print(xs[-2:][0])
print(len(xs[10:]))
