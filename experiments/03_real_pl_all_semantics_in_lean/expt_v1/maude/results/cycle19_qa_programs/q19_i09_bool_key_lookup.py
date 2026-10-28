d = {1: "one", 0: "zero"}
print(d[True])
print(d[False])
e = {True: "T", False: "F"}
print(e[1])
print(e[0])
try:
    print(e[2])
except Exception as ex:
    print("KE")
f = {2: "two"}
try:
    print(f[True])
except Exception as ex:
    print("KE2")
