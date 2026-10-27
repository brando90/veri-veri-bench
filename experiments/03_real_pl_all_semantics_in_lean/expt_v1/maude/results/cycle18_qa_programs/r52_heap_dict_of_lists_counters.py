groups = {}
for i in range(60):
    k = i % 7
    if k in groups:
        groups[k] += [i]
    else:
        groups[k] = [i]
print(groups[3])
print(len(groups))
cnt = {}
for w in ["a", "b", "a", "c", "b", "a"]:
    if w in cnt:
        cnt[w] += 1
    else:
        cnt[w] = 1
print(cnt)
