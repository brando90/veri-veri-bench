xs = [10, 20, 30]
try:
    xs[1] %= 0
except Exception as e:
    print("a")
print(xs)
try:
    xs[-1] //= 0
except Exception as e:
    print("b")
print(xs)
d = {"k": 9}
try:
    d["k"] //= 0
except Exception as e:
    print("c")
print(d)
xs[0] //= 3
d["k"] %= 4
print(xs)
print(d)
