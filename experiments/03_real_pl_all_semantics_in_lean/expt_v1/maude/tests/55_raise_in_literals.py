# a raise inside list / tuple / dict literals, slices and function position propagates
def g(n):
    if n > 1:
        raise Exception(n)
    return n
try:
    xs = [1, g(5), 3]
    print(99)
except Exception as e:
    print(e)
try:
    t = (g(0), g(6))
    print(98)
except Exception as e:
    print(e)
try:
    d = {"a": g(7)}
    print(97)
except Exception as e:
    print(e)
ys = [1, 2, 3, 4]
try:
    zs = ys[g(8):]
    print(96)
except Exception as e:
    print(e)
try:
    zs = ys[0:g(9)]
    print(95)
except Exception as e:
    print(e)
try:
    zs = ys[g(0):g(3)]
    print(94)
except Exception as e:
    print(e)
def pick(n):
    if n > 1:
        raise Exception(n)
    return g
try:
    r = pick(11)(1)
    print(93)
except Exception as e:
    print(e)
try:
    print(len([g(12)]))
except Exception as e:
    print(e)
try:
    print([g(1), g(13)][0])
except Exception as e:
    print(e)
fs = [g]
try:
    q = fs[g(14)](1)
    print(92)
except Exception as e:
    print(e)
s = "hello"
try:
    print(s[g(15):])
except Exception as e:
    print(e)
try:
    print((1, [2, g(16)]))
except Exception as e:
    print(e)
def f(a, b):
    return a
try:
    print(f([1, g(17)], 2))
except Exception as e:
    print(e)
print([g(1), g(0)][1])
