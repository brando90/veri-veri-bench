# conditional expressions and negative indexes
def sign(n):
    return 1 if n > 0 else (0 if n == 0 else -1)
print(sign(5))
print(sign(0))
print(sign(-3))
calls = [0]
def tick():
    calls[0] += 1
    return 1
a = tick() if True else tick() + tick()
print(calls[0])
xs = [1, 2, 3, 4]
print(xs[-1])
print(xs[-4])
xs[-2] = 30
print(xs[2])
t = (7, 8, 9)
print(t[-1])
print(t[-3])
print("yes" if xs[-1] == 4 else "no")
print(len(xs) if xs else 0)
e = []
print(len(e) if e else -1)
