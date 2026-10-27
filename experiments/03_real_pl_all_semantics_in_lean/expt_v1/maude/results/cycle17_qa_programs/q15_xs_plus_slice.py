xs = [1, 2, 3]
al = xs
xs += xs[:]
print(len(al))
print(al[5])
xs += xs[1:3]
print(len(al))
print(al[7])
