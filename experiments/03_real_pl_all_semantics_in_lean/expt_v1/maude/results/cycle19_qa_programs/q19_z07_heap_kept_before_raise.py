log = []
def f(x):
    log.append(x)
    log.append(x // 0)
    log.append(99)
for i in range(3):
    try:
        f(i)
    except Exception as e:
        log.append(-i)
print(log)
xs = [1, 2]
try:
    xs[0] = 5 // 0
except Exception as e:
    print(xs)
d = {1: 1}
try:
    d[2] = 1 % 0
except Exception as e:
    print(d)
