def inner(n):
    loc = [n]
    try:
        if n > 1:
            raise Exception("big")
        return loc
    except Exception as e:
        return [n, n]
def outer():
    a = 1
    r1 = inner(1)
    b = 2
    r2 = inner(5)
    c = a + b
    return len(r1) * 100 + len(r2) * 10 + c
print(outer())
x = 9
print(outer() + x)
