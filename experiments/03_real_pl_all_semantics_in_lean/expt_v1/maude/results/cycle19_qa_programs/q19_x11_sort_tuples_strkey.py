ps = [("bob", 3), ("alice", 5), ("al", 1), ("Bob", 2)]
n = len(ps)
for i in range(n):
    for j in range(n - 1 - i):
        if ps[j][0] > ps[j + 1][0]:
            tmp = ps[j]
            ps[j] = ps[j + 1]
            ps[j + 1] = tmp
print(ps)
