def build(d):
    if d == 0:
        return [0, [], []]
    return [d, build(d - 1), build(d - 1)]
def total(t):
    if len(t[1]) == 0:
        return t[0]
    return t[0] + total(t[1]) + total(t[2])
t = build(6)
print(total(t))
