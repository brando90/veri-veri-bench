def outer():
    x = [1]
    def f():
        return len(x)
    x = [1, 2, 3]
    return f
print(outer()())
