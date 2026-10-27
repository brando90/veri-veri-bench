z = "g"
def a():
    z = "a"
    def b():
        def c():
            return z
        try:
            r = c()
        except Exception as e:
            r = "NE"
        z = "b"
        return r + c()
    return b()
print(a())
