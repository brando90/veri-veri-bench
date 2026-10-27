# a raise from a call nested in larger expressions propagates
def g(n):
    if n > 1:
        raise Exception(n)
    return n
try:
    v = 1 + 2 * g(3)
except Exception as e:
    print(e)
try:
    v = not g(6)
except Exception as e:
    print(e)
try:
    v = 1 and g(7)
except Exception as e:
    print(e)
try:
    v = 0 and g(8)
    print(v)
except Exception as e:
    print(99)
try:
    xs = [1, 2, 3]
    v = xs[g(2)]
except Exception as e:
    print(e)
def safe(n):
    try:
        z = g(n) + 1
        return z
    except Exception as e:
        return 100
print(safe(1))
print(safe(5))
def show(a, b):
    print(a)
    print(b)
try:
    show(1, g(9))
except Exception as e:
    print(e)
try:
    t = g(0) + g(11) + g(12)
except Exception as e:
    print(e)
