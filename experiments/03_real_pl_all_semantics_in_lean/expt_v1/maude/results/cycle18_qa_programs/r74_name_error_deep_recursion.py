def depth(n):
    if n == 0:
        try:
            return missing
        except Exception as e:
            return 0
    return 1 + depth(n - 1)
print(depth(150))
