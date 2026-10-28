ws = ["pear", "Peach", "apple", "app", "", "banana", "band", "ban", "Zeta", "10", "9"]
n = len(ws)
for i in range(n):
    for j in range(n - 1 - i):
        if ws[j] > ws[j + 1]:
            tmp = ws[j]
            ws[j] = ws[j + 1]
            ws[j + 1] = tmp
print(ws)
