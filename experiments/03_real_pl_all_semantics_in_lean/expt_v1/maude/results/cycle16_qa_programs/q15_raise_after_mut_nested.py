d = {}
def g(k):
    d[k] = k * 2
    if k == 3:
        raise Exception(k)
    return g(k + 1)
try:
    g(0)
except Exception as e:
    print(len(d))
print(d[3])
