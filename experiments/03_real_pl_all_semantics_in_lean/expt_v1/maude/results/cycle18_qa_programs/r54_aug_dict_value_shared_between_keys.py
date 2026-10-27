shared = [0]
d = {"a": shared, "b": shared}
d["a"] += [1]
d["b"] *= 2
print(shared)
print(d)
d["a"] = d["a"] + [9]
print(shared)
print(d["a"])
