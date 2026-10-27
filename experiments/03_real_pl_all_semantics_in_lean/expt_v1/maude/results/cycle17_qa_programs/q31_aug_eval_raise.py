xs = [1]
ys = xs
def bad():
    xs.append(5)
    raise Exception("no")
try:
    xs += bad()
except Exception as e:
    print("caught")
print(len(ys))
n = 3
def badn():
    raise Exception("z")
try:
    n += badn()
except Exception as e:
    print(n)
