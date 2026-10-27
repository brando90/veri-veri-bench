def outer(v):
    def get():
        return v
    a = get()
    v = v + 1
    b = get()
    return [a, b]
print(outer(1))
def outer2(v):
    get = lambda: v
    out = []
    for i in range(3):
        out.append(get())
        v = v * 2
    return out
print(outer2(3))
