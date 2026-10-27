def build(d):
    if d == 0:
        return []
    return [build(d - 1), build(d - 1)]
def count(t):
    if len(t) == 0:
        return 1
    return count(t[0]) + count(t[1])
print(count(build(5)))
