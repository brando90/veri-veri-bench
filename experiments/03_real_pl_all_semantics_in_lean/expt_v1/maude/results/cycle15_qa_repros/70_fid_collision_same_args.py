# two activations of a zero-arg function must not be confused
box = []
def f():
    if len(box) == 0:
        x = 1
        def get():
            return x
        box.append(get)
        return 0
    x = 2
    return box[0]()
f()
print(f())
def mk(n):
    xs = [n]
    def peek():
        return len(xs)
    xs.append(n)
    return peek
p1 = mk(1)
p2 = mk(1)
def mk2(n):
    xs = [n, n, n, n]
    return p1() + p2()
print(mk2(1))
