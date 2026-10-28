d = {"a": 1}
d["self"] = d
print(d == d)
print([d] == [d])
e = {"self": d, "a": 1}
print(len(e))
