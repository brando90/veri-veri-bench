vals = [0, 1, "", "a", None, [], [0], (), (0,), {}, {"k": 1}, True, False, -1]
out = []
for v in vals:
    out.append("T" if v else "F")
print(out)
def f():
    return 1
g = f if f else None
print(g())
lam = (lambda: "a") if len(vals) > 3 else (lambda: "b")
print(lam())
