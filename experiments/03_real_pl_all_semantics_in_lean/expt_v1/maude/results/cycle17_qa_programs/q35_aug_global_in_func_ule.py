total = [0]
def add(v):
    total += [v]
    return 1
try:
    add(3)
except Exception as e:
    print("ule")
print(len(total))
def add2(v):
    t = total
    t += [v]
    return len(t)
print(add2(4))
print(len(total))
