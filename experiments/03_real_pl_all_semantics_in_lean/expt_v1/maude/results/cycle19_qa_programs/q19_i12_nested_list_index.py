m = [[1, 2], [3]]
for i in [0, 1, 2, -1, -3]:
    for j in [0, 1, -2]:
        try:
            print(m[i][j])
        except Exception as e:
            print("IE")
