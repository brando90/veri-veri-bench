def mk():
    t = ([], [])
    def add(i, v):
        try:
            t[i] += [v]
        except Exception as e:
            return False
        return True
    return add, t
add, t = mk()
print(add(0, 1))
print(add(1, 2))
print(add(0, 3))
print(t)
