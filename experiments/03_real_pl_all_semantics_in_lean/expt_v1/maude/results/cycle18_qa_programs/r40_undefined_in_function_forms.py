def f():
    out = []
    try:
        out.append(gone)
    except Exception as e:
        out.append(1)
    try:
        gone2[0] += [1]
    except Exception as e:
        out.append(2)
    try:
        gone3.append(1)
    except Exception as e:
        out.append(3)
    try:
        gone4[1] = 2
    except Exception as e:
        out.append(4)
    return out
print(f())
gone = 1
gone2 = [[0]]
gone3 = []
gone4 = [0, 0]
print(f())
print(gone2)
print(gone3)
print(gone4)
