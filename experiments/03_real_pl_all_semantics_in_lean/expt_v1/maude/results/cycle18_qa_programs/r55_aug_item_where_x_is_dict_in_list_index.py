rows = [{"n": 0, "l": []}, {"n": 5, "l": [1]}]
r = rows[1]
r["n"] += 1
r["l"] += [2]
print(rows)
def get(i):
    return i
for i in range(2):
    rr = rows[get(i)]
    rr["n"] *= 2
print(rows)
