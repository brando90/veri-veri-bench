d = {"l": [1, 2]}
d["l"] += d["l"]
print(d)
l = d["l"]
d["l"] *= 2
print(len(l))
d2 = {"x": [1]}
d2["x"] += d2
print(d2["x"])
