def ident(l):
    return l
x = [1]
y = ident(x)
y.append(5)
print(len(x))
print(x[1])
