# reading a variable bound to None
x = None
print(x)
y = x
print(y)
print(x == None)
print(x != None)
x = 5
print(x)
if y == None:
    print(1)
else:
    print(2)
z = None
w = z
if w:
    print(7)
else:
    print(8)
def f(a):
    return a
print(f(None))
r = f(y)
print(r)
