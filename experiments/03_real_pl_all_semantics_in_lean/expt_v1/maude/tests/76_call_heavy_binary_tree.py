# calls inside list literals and argument lists ran several times each before cycle 17; this is fast now
def build(d):
    if d == 0:
        return []
    return [build(d - 1), build(d - 1)]
def count(t):
    if len(t) == 0:
        return 1
    return count(t[0]) + count(t[1])
print(count(build(6)))
def pair(a, b):
    return [a, b]
def deep(d):
    if d == 0:
        return 0
    return len(pair(deep(d - 1), deep(d - 1)))
print(deep(6))
def tup(d):
    if d == 0:
        return 1
    t = (tup(d - 1), tup(d - 1))
    return t[0] + t[1]
print(tup(7))
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print(fib(12))
