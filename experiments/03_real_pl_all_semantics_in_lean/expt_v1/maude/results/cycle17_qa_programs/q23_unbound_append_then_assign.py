xs = [1]
def f():
    xs.append(2)
    xs = []
    return 0
try:
    f()
except Exception as e:
    print("ule")
print(len(xs))
