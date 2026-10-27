def addk(d, k, v):
    d[k] = v
    return d
a = {}
b = addk(addk(a, 'x', 1), 'y', 2)
print(len(a))
b['z'] = 3
print(len(a))
