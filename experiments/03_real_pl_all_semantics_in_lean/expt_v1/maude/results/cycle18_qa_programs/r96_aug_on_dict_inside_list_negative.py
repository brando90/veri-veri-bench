data = [{"c": 0}, {"c": 10}]
last = data[-1]
for i in range(3):
    dd = data[-1]
    dd["c"] += i
print(last)
lists = [[], []]
first = lists[-2]
for i in range(4):
    lists[-2 + i % 2] += [i]
print(first)
print(lists)
