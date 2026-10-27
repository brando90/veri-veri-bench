def mk(base):
    def ev(n):
        if n == 0:
            return base
        return od(n - 1)
    def od(n):
        if n == 0:
            return base + 1
        return ev(n - 1)
    return ev
e1 = mk(10)
e2 = mk(20)
print(e1(7))
print(e2(8))
print(e1(4))
