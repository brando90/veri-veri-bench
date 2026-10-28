# t[0] += x on a tuple raises TypeError; the list inside is still changed first (CPython)
inner = [1]
t = (inner, 5)
try:
    t[0] += [2]
except Exception as e:
    print(100)
print(len(inner))
print(inner[1])
print(len(t[0]))
u = (1, 2)
try:
    u[0] += 1
except Exception as e:
    print(200)
print(u[0])
try:
    u[1] *= 3
except Exception as e:
    print(300)
print(u[1])
try:
    u[0] = 9
except Exception as e:
    print(400)
print(u[0])
w = ([0], [1])
try:
    w[1] *= 2
except Exception as e:
    print(500)
print(len(w[1]))
s = "abc"
try:
    s[0] = "x"
except Exception as e:
    print(600)
print(s)
def f():
    q = (1, 2, 3)
    try:
        q[-1] += 1
    except Exception as e:
        return q[-1]
print(f())
lst = [[1]]
lst[0] += [2]
print(len(lst[0]))
