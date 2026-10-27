inner = {'k': 1}
outer = {'x': inner}
inner['k'] = 2
print(outer['x']['k'])
o2 = outer['x']
o2['j'] = 3
print(len(inner))
