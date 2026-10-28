def p(v):
    print(v)
    return v
try:
    xs = [p(1), p(2) // 0, p(3)]
except Exception as e:
    print("list")
try:
    t = (p(4), p(5) % 0, p(6))
except Exception as e:
    print("tup")
try:
    d = {p(7): p(8), p(9) // 0: p(10)}
except Exception as e:
    print("dict")
ys = [1, 2, 3, 4]
try:
    print(ys[p(1):p(4) // 0])
except Exception as e:
    print("slice")
def f(a, b):
    return a + b
try:
    print(f(p(11), p(12) // 0))
except Exception as e:
    print("call")
