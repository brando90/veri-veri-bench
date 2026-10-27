t = ([1],)
try:
    t[0] += [2]
except Exception as e:
    print("TypeError")
print(t)
