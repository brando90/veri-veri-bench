def upd(box, i, f):
    try:
        box[i] += f()
    except Exception as e:
        print(e)
        return "err"
    return "ok"
def ok():
    return [1]
def bad():
    raise Exception("bad")
b = [[0]]
k = b[0]
print(upd(b, 0, ok))
print(upd(b, 0, bad))
print(upd(b, -1, ok))
print(k)
