def outer():
    x = 1
    def r():
        return x
    a = r()
    x = 2
    b = r()
    return [a, b]
print(outer())
def outer2():
    def r():
        return x
    out = []
    for i in range(3):
        try:
            out.append(r())
        except Exception as e:
            out.append("NE")
        x = i
    return out
print(outer2())
