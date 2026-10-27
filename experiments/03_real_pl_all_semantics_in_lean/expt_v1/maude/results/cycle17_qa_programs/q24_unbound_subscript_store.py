d = {"a": 1}
def f():
    d["a"] = 2
    d = {}
    return 0
try:
    f()
except Exception as e:
    print("ule")
print(d["a"])
