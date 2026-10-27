def f(l):
    l.append(1)
    l = [7, 7, 7]
    l.append(2)
    return len(l)
x = [0]
print(f(x))
print(len(x))
