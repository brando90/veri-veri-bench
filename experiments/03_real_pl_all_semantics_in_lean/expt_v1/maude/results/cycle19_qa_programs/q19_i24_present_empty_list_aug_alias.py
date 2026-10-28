inner = []
d = {"k": inner}
d["k"] += [1]
print(inner)
try:
    d["j"] += [2]
except Exception as e:
    print("KE")
print(d)
