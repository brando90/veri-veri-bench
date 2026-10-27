def build(n):
    if n == 0:
        return lambda: 0
    prev = build(n - 1)
    return lambda: prev() + 1
f = build(300)
print(f())
def count(n, acc):
    if n == 0:
        return len(acc)
    acc += [n]
    return count(n - 1, acc)
print(count(300, []))
