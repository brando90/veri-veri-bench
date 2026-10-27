def counter():
    box = [0]
    def inc():
        box[0] = box[0] + 1
        return box[0]
    def get():
        return box[0]
    return [inc, get]
c1 = counter()
c2 = counter()
c1[0]()
c1[0]()
c2[0]()
print(c1[1]())
print(c2[1]())
def wrap(f):
    k = 100
    return lambda: f() + k
w = wrap(c1[0])
print(w())
print(c1[1]())
