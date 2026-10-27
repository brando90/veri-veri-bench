# parameters shadow caller and global variables in nested and recursive calls
n = 3
def count(n):
    if n <= 0:
        return 0
    return n + count(n - 1)
print(count(4))
print(n)
x = 1
def outer(x):
    def mid(x):
        return x * 10
    y = mid(x + 1)
    return x + y
print(outer(5))
print(x)
def swap_sum(a, b):
    t = a
    a = b
    b = t
    return a * 10 + b
a = 1
b = 2
print(swap_sum(b, a))
print(a)
print(b)
def make(k):
    def add(v):
        return v + k
    return add
k = 1000
print(make(5)(1))
print(k)
