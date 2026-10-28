def length(xs, i):
    try:
        v = xs[i]
    except Exception as e:
        return i
    return length(xs, i + 1)
print(length([1, 2, 3, 4], 0))
print(length("hello!", 0))
print(length((), 0))
