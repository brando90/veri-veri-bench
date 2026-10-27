def outer(n):
    def ev(k):
        if k == 0:
            return True
        return od(k - 1)
    def od(k):
        if k == 0:
            return False
        return ev(k - 1)
    return ev(n)
if outer(10):
    print(1)
else:
    print(0)
if outer(7):
    print(1)
else:
    print(0)
