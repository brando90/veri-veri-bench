# a parameter mutated and then rebound; a parameter rebound and then mutated
def f(xs):
    xs.append(1)
    xs = [9]
    return len(xs)
a = [0]
print(f(a))
print(len(a))
print(a[0])
def g(xs):
    xs = [7]
    xs.append(1)
    return len(xs)
b = [0]
print(g(b))
print(len(b))
print(b[0])
