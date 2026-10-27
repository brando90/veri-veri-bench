k = 3
def f(flag):
    if flag:
        k = 10
    else:
        pass
    return k
print(f(True))
try:
    print(f(False))
except Exception as e:
    print("ule")
print(k)
