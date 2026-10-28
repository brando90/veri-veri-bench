for xs in [[], [7], [1, 2, 3, 4, 5]]:
    n = len(xs)
    for i in [n - 1, n, -n, -n - 1, 0, -1]:
        try:
            print(xs[i])
        except Exception as e:
            print("IE")
