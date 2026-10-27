def f(l):
    l.append(1)
    raise Exception(5)
x = []
try:
    f(x)
except Exception as e:
    print(len(x))
print(len(x))
