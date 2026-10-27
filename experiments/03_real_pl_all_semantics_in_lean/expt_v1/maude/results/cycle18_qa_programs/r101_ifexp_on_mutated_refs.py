c = []
d = {}
print("T" if c else "F")
c.append(0)
d["k"] = 0
print("T" if c else "F")
print("T" if d else "F")
e = c
e *= 0
print("T" if c else "F")
