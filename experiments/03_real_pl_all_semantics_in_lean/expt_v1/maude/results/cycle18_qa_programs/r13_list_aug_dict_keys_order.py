d = {"b": 1, "a": 2}
d["c"] = 3
d["b"] = 10
xs = [0]
xs += d
print(xs)
e = {}
xs += e
print(xs)
xs += ""
xs += ()
print(len(xs))
