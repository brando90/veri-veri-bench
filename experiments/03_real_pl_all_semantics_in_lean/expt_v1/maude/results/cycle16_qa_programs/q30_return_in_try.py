def f(l):
    try:
        l.append(1)
        return len(l)
    except Exception as e:
        return 0 - 1
x = [5]
print(f(x))
print(f(x))
