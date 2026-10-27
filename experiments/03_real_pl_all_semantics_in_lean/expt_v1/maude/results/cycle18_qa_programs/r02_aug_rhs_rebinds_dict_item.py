d = {"k": [1]}
keep = d["k"]
def g():
    d["k"] = "replaced"
    return [2, 3]
d["k"] += g()
print(d["k"])
print(keep)
