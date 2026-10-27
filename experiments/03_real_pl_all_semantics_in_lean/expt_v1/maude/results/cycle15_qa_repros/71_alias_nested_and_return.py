# mutation through aliases: nested lists, returned lists, local aliases
def addrow(row):
    row.append(1)
    return len(row)
grid = [[0], [0]]
print(addrow(grid[0]))
print(len(grid[0]))
def ident(xs):
    return xs
a = [1]
b = ident(a)
b.append(2)
print(len(a))
def viaalias(xs):
    ys = xs
    ys.append(3)
    return len(xs)
print(viaalias(a))
print(len(a))
def gpush(v):
    store.append(v)
    return len(store)
store = [0]
def both(ys):
    ys.append(1)
    gpush(2)
    return len(ys)
print(both(store))
print(len(store))
