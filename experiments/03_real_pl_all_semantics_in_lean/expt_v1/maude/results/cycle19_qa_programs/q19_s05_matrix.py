ws = ["b", "ab", "a", "", "ba", "B", "aa"]
for x in ws:
    row = []
    for y in ws:
        row.append(x < y)
    print(row)
