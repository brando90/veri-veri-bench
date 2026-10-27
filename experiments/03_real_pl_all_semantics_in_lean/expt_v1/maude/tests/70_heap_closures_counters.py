# closures with their own heap state: independent counters, shared state between closures, recursion
def counter():
    c = []
    def inc():
        c.append(1)
        return len(c)
    return inc
a = counter()
b = counter()
print(a())
print(a())
print(b())
print(a() + b())
def pair():
    log = []
    def put(v):
        log.append(v)
        return len(log)
    def size():
        return len(log)
    return put, size
put, size = pair()
put(1)
put(2)
print(size())
p2, s2 = pair()
print(s2())
def fib_list(n):
    out = [0, 1]
    def go(k):
        if k >= n:
            return len(out)
        out.append(out[k - 1] + out[k - 2])
        return go(k + 1)
    return go(2)
print(fib_list(10))
def depth(n, acc):
    acc.append(n)
    if n == 0:
        return len(acc)
    return depth(n - 1, acc)
box = []
print(depth(5, box))
print(len(box))
print(box[0] + box[5])
def outer():
    xs = []
    def mid():
        def inner(v):
            xs.append(v)
            return len(xs)
        return inner
    f = mid()
    f(1)
    f(2)
    return len(xs)
print(outer())
