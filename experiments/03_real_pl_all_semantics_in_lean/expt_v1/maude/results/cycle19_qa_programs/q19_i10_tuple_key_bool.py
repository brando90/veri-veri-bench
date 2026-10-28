d = {(1, 0): "a", ((1,), 2): "b"}
print(d[(True, False)])
print(d[((True,), 2)])
try:
    print(d[(1, 1)])
except Exception as e:
    print("KE")
d[(True, 0)] = "c"
print(d)
print(len(d))
