store = []
for i in range(300):
    store.append([i])
for i in range(300):
    store[i] += [i * 2]
total = 0
for i in range(300):
    total += store[i][1] - store[i][0]
print(total)
alias = store[123]
s123 = store[123]
s123[0] = -1
print(alias)
print(store[299])
