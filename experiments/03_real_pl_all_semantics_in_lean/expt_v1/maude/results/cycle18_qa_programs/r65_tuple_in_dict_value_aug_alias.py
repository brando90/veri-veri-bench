d = {"t": (1,)}
snap = d["t"]
d["t"] += d["t"]
print(snap)
print(d["t"])
d["t"] *= 2
print(len(d["t"]))
