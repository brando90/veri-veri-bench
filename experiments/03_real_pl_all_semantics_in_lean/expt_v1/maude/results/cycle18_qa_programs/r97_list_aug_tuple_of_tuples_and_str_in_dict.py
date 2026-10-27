d = {"l": ["x"]}
d["l"] += "yz"
d["l"] += (("a", 1),)
d["l"] += {"k1": 1, "k2": 2}
print(d)
print(len(d["l"]))
