d = {"a": 1}
def add():
    d["b"] = 2
    d["c"] = [3]
    return 10
d["a"] += add()
print(d)
c = d["c"]
d["c"] += [add()]
print(c)
print(d)
