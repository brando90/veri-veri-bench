n = [1, 2, 3]
def bump():
    n[1] = 50
    return 4
n[1] += bump()
print(n)
d = {"a": 1}
def setd():
    d["a"] = 100
    d["b"] = 7
    return 2
d["a"] *= setd()
print(d["a"])
print(d["b"])
print(len(d))
