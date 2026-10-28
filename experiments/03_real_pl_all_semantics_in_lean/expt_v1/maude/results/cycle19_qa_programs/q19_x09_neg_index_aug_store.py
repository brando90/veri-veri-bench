xs = [[1], [2], [3]]
alias = xs[-1]
xs[-1] += [4]
print(alias)
try:
    xs[-4] += [5]
except Exception as e:
    print("IE")
xs[-3] = "a"
print(xs)
