# reading a local before it is assigned raises UnboundLocalError (caught here by a bare except)
x = 1
def f():
    y = x
    x = 2
    return y
try:
    print(f())
except Exception as e:
    print(99)
# a global of the same name is read normally when the function never assigns it
def g():
    return x
print(g())
# assigned later in the body, read before: local, so it raises
def h():
    try:
        print(z)
    except Exception as err:
        print(98)
    z = 5
    return z
z = 4
print(h())
# assigned in only one branch
def k(flag):
    if flag:
        w = 1
    return w
w = 7
print(k(True))
try:
    print(k(False))
except Exception as e2:
    print(97)
# augmented assignment on an unassigned local also raises
c = 10
def m():
    c += 1
    return c
try:
    print(m())
except Exception as e3:
    print(96)
print(c)
# a parameter is always bound
def p(q):
    q = q + 1
    return q
print(p(1))
# a closure reads the enclosing function's variable, assigned before the call
def outer():
    v = 3
    def inner():
        return v
    return inner()
print(outer())
