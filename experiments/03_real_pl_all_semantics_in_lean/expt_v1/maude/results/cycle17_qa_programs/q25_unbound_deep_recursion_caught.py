z = 1
def rec(n):
    if n == 0:
        y = z
        z = 2
        return y
    keep = n * 3
    r = rec(n - 1)
    return r + keep
try:
    print(rec(5))
except Exception as e:
    print("ule")
def ok(n):
    if n == 0:
        return 0
    return n + ok(n - 1)
print(ok(10))
print(z)
