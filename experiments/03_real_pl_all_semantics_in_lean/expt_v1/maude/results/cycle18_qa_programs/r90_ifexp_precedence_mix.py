a = 0
b = 5
print(a if b else 3 or 4)
print((a if a else b) + 1)
print(1 + (2 if a else 3) * 2)
print(not a if b else a)
f = lambda x: "neg" if x < 0 else "zero" if x == 0 else "pos"
print(f(-1))
print(f(0))
print(f(9))
