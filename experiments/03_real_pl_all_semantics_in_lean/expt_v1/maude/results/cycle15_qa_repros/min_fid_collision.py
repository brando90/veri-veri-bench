box = []
def f():
    if len(box) == 0:
        x = 1
        def get():
            return x
        box.append(get)
        return 0
    x = 2
    return box[0]()
f()
print(f())
