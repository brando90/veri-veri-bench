# list mutation in callees: params, globals, recursion, local shadowing
def fill(xs, n):
    if n > 0:
        xs.append(n)
        fill(xs, n - 1)
acc = []
fill(acc, 4)
print(len(acc))
print(acc[0])
print(acc[3])
res = []
def helper():
    res = []
    res.append(1)
    res.append(2)
    res.append(3)
def driver():
    res = []
    helper()
    print(len(res))
    res.append(5)
    print(len(res))
driver()
print(len(res))
def two(p, q):
    p.append(1)
    q.append(2)
    q.append(3)
l1 = []
l2 = []
two(l1, l2)
print(len(l1))
print(len(l2))
g2 = [0]
def bump():
    g2[0] = g2[0] + 1
bump()
bump()
bump()
print(g2[0])
def nested_global():
    bump()
    bump()
nested_global()
print(g2[0])
