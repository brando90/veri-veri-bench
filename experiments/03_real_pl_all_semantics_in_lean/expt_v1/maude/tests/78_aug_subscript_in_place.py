# x[i] op= e on a subscript target: a list item is extended / repeated in place, so aliases see it
a = [[1]]
inner = a[0]
a[0] += [9]
print(len(inner))
print(inner[1])
d = {"k": [1]}
v = d["k"]
d["k"] += [2, 3]
print(len(v))
print(len(d["k"]))
n = [10, 20, 30]
n[1] += 5
n[2] -= 7
n[0] *= 3
print(n[0])
print(n[1])
print(n[2])
n[0] //= 4
n[1] %= 6
print(n[0])
print(n[1])
m = [[1, 2], [3]]
alias = m[1]
m[1] *= 3
print(len(alias))
print(len(m[1]))
neg = [1, 2, 3]
neg[-1] += 10
print(neg[2])
words = {"a": "x"}
words["a"] += "y"
print(words["a"])
cnt = {"z": 0}
cnt["z"] += 1
cnt["z"] += 1
print(cnt["z"])
# the index expression is evaluated once, before the right-hand side
log = [0]
def idx():
    log.append(1)
    return 0
q = [5]
q[idx()] += 2
print(len(log))
print(q[0])
def grow(box):
    box[0] += [7]
b = [[1]]
keep = b[0]
grow(b)
grow(b)
print(len(keep))
