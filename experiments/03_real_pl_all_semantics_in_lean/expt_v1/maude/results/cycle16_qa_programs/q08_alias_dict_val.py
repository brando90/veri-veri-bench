x = [1, 2]
d = {'a': x, 'b': x}
y = d['a']
y.append(3)
print(len(d['b']))
print(len(x))
