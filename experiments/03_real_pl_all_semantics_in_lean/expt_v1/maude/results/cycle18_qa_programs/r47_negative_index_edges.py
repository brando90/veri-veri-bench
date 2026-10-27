xs = [10, 20, 30]
print(xs[-3])
print(xs[-0])
xs[-3] = 1
xs[-1] = 3
print(xs)
t = (1, (2, 3), [4])
print(t[-2][-1])
tl = t[-1]
tl[-1] = 40
print(t)
nested = [[1, 2], [3, 4]]
nl = nested[-1]
nl[-2] = 33
print(nested)
k = -1
print(xs[k - 1])
print(xs[len(xs) * -1])
