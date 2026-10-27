acc = [0]
def bad():
    local_list = [1, 2]
    acc.append(len(local_list))
    v = u
    u = 1
    return v
def good(n):
    s = 0
    for i in range(n):
        s += i
    return s
for k in range(3):
    try:
        bad()
    except Exception as e:
        acc.append(good(k + 3))
print(len(acc))
for v in acc:
    print(v)
