def mk():
    n = [0]
    def step(k):
        n[0] = n[0] + 1
        return 100 // k
    return step, n
step, n = mk()
out = []
for k in [5, 0, 2, 0, 1]:
    try:
        out.append(step(k))
    except Exception as e:
        out.append(-1)
        continue
    if k == 1:
        break
print(out)
print(n)
