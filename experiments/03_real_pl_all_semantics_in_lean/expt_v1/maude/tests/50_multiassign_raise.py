# a raise from the right side of a tuple assignment propagates
def pair(n):
    if n > 0:
        raise Exception(n)
    return (1, 2)
a = 0
try:
    a, b = pair(4)
    a = 99
except Exception as e:
    print(a)
    print(e)
c, d = pair(0)
print(c + d)
