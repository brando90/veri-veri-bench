grid = [[1], [2], [3]]
for row in grid:
    row += [0]
    row *= 2
for row in grid:
    print(len(row))
print(grid[1][2])
k = 3
ys = [7]
ys *= k
ys *= len(ys)
print(len(ys))
