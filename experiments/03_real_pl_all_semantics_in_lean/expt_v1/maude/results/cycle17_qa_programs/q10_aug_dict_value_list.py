d = {"k": [1]}
v = d["k"]
d["k"] += [2]
print(len(v))
print(len(d["k"]))
