def f(n):
    out = []
    for i in range(n):
        if i > 0:
            out.append(t)
        t = i * 10
    return len(out)
print(f(3))
def g(n):
    out = []
    for i in range(n):
        out.append(t)
        t = i
    return len(out)
t = 99
try:
    print(g(3))
except Exception as e:
    print("ule")
