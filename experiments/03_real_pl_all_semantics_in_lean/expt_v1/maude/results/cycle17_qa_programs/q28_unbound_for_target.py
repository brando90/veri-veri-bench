i = 50
def f():
    r = i
    for i in range(3):
        pass
    return r
try:
    print(f())
except Exception as e:
    print("ule")
def g(n):
    for j in range(n):
        pass
    return j
print(g(4))
try:
    print(g(0))
except Exception as e:
    print("ule2")
