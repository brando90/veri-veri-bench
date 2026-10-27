# a raise through a chain of calls in operand position is linear, not exponential
def f0(n):
    raise Exception(n)
def f1(n):
    return f0(n) + 1
def f2(n):
    return f1(n) + 1
def f3(n):
    return f2(n) + 1
def f4(n):
    return f3(n) + 1
def f5(n):
    return f4(n) + 1
def f6(n):
    return f5(n) + 1
def f7(n):
    return f6(n) + 1
def f8(n):
    return f7(n) + 1
def f9(n):
    return f8(n) + 1
try:
    v = f9(5)
except Exception as e:
    print(e)
def d0(n):
    raise Exception(n)
def d1(n):
    return (1 + d0(n) * 2) - 3
def d2(n):
    return (1 + d1(n) * 2) - 3
def d3(n):
    return (1 + d2(n) * 2) - 3
def d4(n):
    return (1 + d3(n) * 2) - 3
def d5(n):
    return (1 + d4(n) * 2) - 3
def d6(n):
    return (1 + d5(n) * 2) - 3
def d7(n):
    return (1 + d6(n) * 2) - 3
try:
    w = d7(6)
except Exception as e:
    print(e)
