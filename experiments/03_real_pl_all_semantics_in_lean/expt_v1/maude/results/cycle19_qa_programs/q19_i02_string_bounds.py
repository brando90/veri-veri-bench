for s in ["", "a", "hello"]:
    n = len(s)
    for i in [n - 1, n, -n, -n - 1, 0, -1]:
        try:
            print(s[i])
        except Exception as e:
            print("IE")
