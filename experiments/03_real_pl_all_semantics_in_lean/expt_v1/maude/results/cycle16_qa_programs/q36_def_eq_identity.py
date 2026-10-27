def mk():
    def g():
        return 1
    return g
a = mk()
b = mk()
if a == b:
    print(1)
else:
    print(0)
def same():
    return 0
s1 = same
if s1 == same:
    print(1)
else:
    print(0)
