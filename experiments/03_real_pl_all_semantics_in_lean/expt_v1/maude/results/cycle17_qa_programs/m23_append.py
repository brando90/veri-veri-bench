xs = [1]
def f():
    xs.append(2)
    xs = []
try:
    f()
except Exception as e:
    print("ule")
print(len(xs))
