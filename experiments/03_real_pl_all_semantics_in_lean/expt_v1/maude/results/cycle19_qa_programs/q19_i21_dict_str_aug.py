d = {"x": "a"}
d["x"] += "b"
try:
    d["y"] += "c"
except Exception as e:
    d["y"] = "c"
d["y"] *= 3
print(d)
