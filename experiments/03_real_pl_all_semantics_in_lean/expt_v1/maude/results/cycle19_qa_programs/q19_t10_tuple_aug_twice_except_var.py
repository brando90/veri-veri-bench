t = ([1],)
try:
    t[0] += [2]
except Exception as e:
    print("first")
try:
    print(e)
except Exception as e2:
    print("deleted")
try:
    t[0] += [3]
except Exception as e:
    print("second")
print(t)
