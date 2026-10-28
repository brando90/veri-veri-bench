# 1 // 0 and 1 % 0 raise a catchable exception (CPython: ZeroDivisionError) instead of getting stuck
def f(a, b):
    try:
        return a // b
    except Exception as e:
        return -1
print(f(7, 2))
print(f(7, 0))
print(f(-7, 0))
m = 5
try:
    m = m % 0
except Exception as e:
    print(99)
print(m)
n = 3
try:
    n //= 0
except Exception as e:
    n = -n
print(n)
xs = [4, 8]
try:
    xs[0] //= 0
except Exception as e:
    print(len(xs))
print(xs[0])
k = 0
while k < 3:
    try:
        print(10 // (k - 1))
    except Exception as e:
        print(-100)
    k += 1
try:
    print(1 + (2 // 0))
except Exception as e:
    print(7)
try:
    print(0 // 0)
except Exception as e:
    print(8)
