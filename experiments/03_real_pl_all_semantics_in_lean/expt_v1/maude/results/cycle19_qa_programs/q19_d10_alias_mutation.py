d1 = {"x": 1}
d2 = d1
d2["y"] = 2
d3 = {"y": 2, "x": 1}
print(d1 == d3)
d3["z"] = [1]
d1["z"] = [True]
print(d1 == d3)
d1["z"] += [2]
print(d1 == d3)
