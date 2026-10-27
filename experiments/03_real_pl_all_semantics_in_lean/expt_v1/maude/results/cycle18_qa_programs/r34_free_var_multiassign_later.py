p = 1
q = 2
def outer():
    def both():
        return p + q
    try:
        r = both()
    except Exception as e:
        r = 0
    p, q = 10, 20
    return r + both()
print(outer())
