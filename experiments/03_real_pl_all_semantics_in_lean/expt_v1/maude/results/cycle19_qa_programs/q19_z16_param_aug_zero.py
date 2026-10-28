def g(x, d):
    try:
        x //= d
    except Exception as e:
        x = x * 10
    return x
print(g(7, 0))
print(g(7, 2))
def h(x):
    def inner():
        return x % 0
    try:
        return inner()
    except Exception as e:
        return x
print(h(42))
