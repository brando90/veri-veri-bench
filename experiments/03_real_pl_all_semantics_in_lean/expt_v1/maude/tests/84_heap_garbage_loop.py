# many short-lived lists and dicts across calls and loops
def mk(i):
    return [i, i + 1]
def mkd(i):
    return {"a": i}
total = 0
for i in range(150):
    l = mk(i)
    d = mkd(i)
    total += l[1] + d["a"]
print(total)
def build(n):
    if n == 0:
        return []
    return [build(n - 1), build(n - 1)]
def size(t):
    if len(t) == 0:
        return 1
    return size(t[0]) + size(t[1])
print(size(build(7)))
acc = []
i = 0
while i < 60:
    acc += [i]
    i += 1
print(len(acc))
