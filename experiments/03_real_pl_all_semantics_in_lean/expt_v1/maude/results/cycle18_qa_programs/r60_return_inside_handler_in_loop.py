def find(xs, target):
    i = 0
    while i < len(xs):
        try:
            if xs[i] == target:
                raise Exception(i)
        except Exception as pos:
            return i * 10
        i += 1
    return -1
print(find([4, 5, 6], 6))
print(find([4, 5, 6], 7))
