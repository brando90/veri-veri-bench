# a parameter that shadows a caller's variable reads the argument, not the caller's value
x = 100
def f(x):
    return x + 1
print(f(5))
print(x)
a = 7
def g(a, b):
    a = a + b
    return a
print(g(1, 2))
print(a)
def h(n):
    def inner(n):
        return n * 2
    return inner(n + 1)
n = 50
print(h(3))
print(n)
k = 1
def twice(k):
    return k + k
print(twice(k + 4))
print(k)
