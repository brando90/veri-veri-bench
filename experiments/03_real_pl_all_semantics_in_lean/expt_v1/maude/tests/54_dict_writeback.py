# dict mutation in a callee is visible to the caller, in statement and expression position
def put(d, k, v):
    d[k] = v
    return len(d)
cfg = {"a": 1}
put(cfg, "b", 2)
print(len(cfg))
n = put(cfg, "c", 3)
print(n)
print(len(cfg))
print(cfg["c"])
reg = {}
def register(name, val):
    reg[name] = val
    return len(reg)
print(register("x", 10))
print(register("y", 20))
print(len(reg))
print(reg["y"])
def local_dict():
    reg = {}
    reg["z"] = 1
    return len(reg)
print(local_dict())
print(len(reg))
def rebind(d):
    d = {"q": 1, "r": 2, "s": 3}
    return len(d)
print(rebind(cfg))
print(len(cfg))
def chain(d):
    return put(d, "deep", 9)
print(chain(cfg))
print(len(cfg))
