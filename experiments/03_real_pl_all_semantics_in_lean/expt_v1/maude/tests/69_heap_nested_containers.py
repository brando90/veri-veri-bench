# nested lists, a list in a dict, a dict in a list, a list in a tuple: all shared through refs
grid = [[0], [0], [0]]
row = grid[1]
row.append(5)
print(len(grid[1]))
last = grid[2]
last[0] = 8
print(grid[2][0])
d = {"a": [1], "b": [2]}
da = d["a"]
da.append(3)
print(len(d["a"]))
e = d["b"]
e.append(4)
print(len(d["b"]))
lst = [{"k": 1}]
m = lst[0]
m["j"] = 2
print(len(lst[0]))
def grow(box):
    first = box[0]
    first.append(1)
    inner = box[1]
    inner["z"] = 1
    return len(box[0]) + len(box[1])
pair = ([0], {"y": 0})
print(grow(pair))
print(len(pair[0]))
print(len(pair[1]))
print(grow(pair))
def mk():
    return [[1, 2], [3]]
q = mk()
r = mk()
q0 = q[0]
q0.append(9)
print(len(q[0]))
print(len(r[0]))
print(len(q) + len(r))
