x = []
d = {'t': (x, 1)}
t = d['t']
l = t[0]
l.append(5)
print(len(x))
print(d['t'][0][0])
