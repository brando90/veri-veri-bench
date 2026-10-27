grid = [[[0]], [[1]]]
row = grid[1]
cell = row[0]
row[0] += [2]
print(cell)
print(grid)
grid[0] *= 2
print(grid[0])
g00 = grid[0][0]
g00.append(5)
print(grid[0])
