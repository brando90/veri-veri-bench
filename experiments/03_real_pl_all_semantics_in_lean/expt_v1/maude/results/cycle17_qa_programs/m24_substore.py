d = {"a": 1}
def f():
    d["a"] = 2
    d = {}
try:
    f()
except Exception as e:
    print("ule")
print(d["a"])
