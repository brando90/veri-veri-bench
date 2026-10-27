# a closure called from a function with a same-named local reads its own variable
def outer():
    x = 5
    def inner():
        return x
    return inner
def caller():
    x = 9
    g = outer()
    return g() + x
print(caller())
def mk(n):
    def get():
        return n
    return get
def user(n):
    f = mk(n + 1)
    return f() * 100 + n
print(user(3))
h = mk(4)
def user2():
    n = 77
    return h() + n
print(user2())
def counter():
    base = 10
    def add(k):
        return base + k
    base = 20
    return add(1)
print(counter())
def rec(n):
    def go(k):
        if k == 0:
            return 0
        return k + go(k - 1)
    return go(n)
print(rec(5))
