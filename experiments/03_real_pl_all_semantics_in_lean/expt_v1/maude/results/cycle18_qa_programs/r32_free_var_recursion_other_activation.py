v = "global"
def f(n, g):
    if n == 0:
        def reader():
            return v
        try:
            return f(1, reader)
        except Exception as e:
            return "NE"
    v = "local" + "1"
    return g()
print(f(0, None))
