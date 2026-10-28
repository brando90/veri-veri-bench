# bool behaves as int in arithmetic, comparison, equality, indexing and dict keys
def b(x):
    if x:
        print(1)
    else:
        print(0)
b(True == 1)
b(1 == True)
b(False == 0)
b(True == 2)
b(True != 1)
b(True == True)
b(True == False)
b(True == "1")
print(True + 1)
print(1 + True)
print(True + True)
print(False * 5)
print(True * 7)
print(10 - True)
print(-True)
print(-False)
print(7 // True)
print(7 % (True + 1))
b(True < 2)
b(True >= 1)
b(False > True)
b(True <= True)
b([True] == [1])
b([1, 2] == [1, True])
b((1, 2) == (True, 2))
b((1, 2) == (True, 3))
b([True, [False]] == [1, [0]])
xs = [10, 20, 30]
print(xs[True])
print(xs[False])
d = {1: 5, 2: 6}
print(d[True])
b(True in d)
b(False in d)
e = {True: 1}
b(e == {1: 1})
b({1: 1} == e)
b(e == {1: 2})
e[1] = 9
print(len(e))
print(e[True])
f = {1: "a", True: "b"}
print(len(f))
print(len(f[1]))
n = 5
n += True
print(n)
n *= True
print(n)
ys = [1, 2]
ys[True] += True
print(ys[1])
