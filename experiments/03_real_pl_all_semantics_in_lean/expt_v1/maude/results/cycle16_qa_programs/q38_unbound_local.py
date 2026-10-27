x = 1
def f():
    y = x
    x = 2
    return y
try:
    print(f())
except Exception as e:
    print(99)
