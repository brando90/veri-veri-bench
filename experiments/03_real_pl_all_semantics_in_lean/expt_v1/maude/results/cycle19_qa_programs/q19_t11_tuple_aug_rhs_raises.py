inner = [1]
t = (inner,)
try:
    t[0] += [1 // 0]
except Exception as e:
    print("ZE")
print(t)
