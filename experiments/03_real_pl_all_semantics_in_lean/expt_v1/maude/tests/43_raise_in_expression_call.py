# a raise from a call in expression position propagates instead of leaving the program stuck
def g(n):
    if n > 1:
        raise Exception(n)
    return n
y = 0
try:
    y = g(2)
    y = 99
except Exception as e:
    print(y)
    print(e)
try:
    print(g(5))
except Exception as e:
    print(e)
def f(n):
    z = g(n)
    return z
try:
    q = f(3)
except Exception as e:
    print(e)
print(g(1))
def pick(a, b):
    return a + b
try:
    r = pick(1, g(4))
except Exception as e:
    print(e)
def thrower(n):
    raise Exception(n)
c = 0
try:
    if thrower(8):
        c = 1
except Exception as e:
    print(e)
try:
    w = 0
    while g(w + 2) > 0:
        w = w + 1
except Exception as e:
    print(e)
print(w)
