d = {"n": None, "z": 0, "s": "", "l": [], "f": False, "t": ()}
for k in ["n", "z", "s", "l", "f", "t", "x"]:
    try:
        v = d[k]
        print(len([v]))
    except Exception as e:
        print("KE")
d["z"] += 1
d["l"] += [1]
d["s"] += "a"
print(d)
