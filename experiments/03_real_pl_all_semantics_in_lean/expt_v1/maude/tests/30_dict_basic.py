d = {"a": 1, "b": 2, "c": 3}
print(d["a"])
print(d["b"])
print(d["c"])
print(len(d))

# update + insert
d["a"] = 100
print(d["a"])
print(len(d))
d["new"] = 7
print(d["new"])
print(len(d))

# empty dict
empty = {}
print(len(empty))
if empty:
    print("nonempty")
else:
    print("empty")
