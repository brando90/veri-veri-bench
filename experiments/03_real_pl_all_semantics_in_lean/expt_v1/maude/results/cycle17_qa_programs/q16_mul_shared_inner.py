row = [[0]]
alias = row
row *= 3
first = row[0]
first.append(1)
print(len(row[2]))
print(len(alias))
row *= 0
print(len(alias))
