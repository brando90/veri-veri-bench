d = {}
try:
    print(d[None])
except Exception as e:
    print("KE")
d[None] = 0
print(d[None])
d[None] += 5
print(d)
