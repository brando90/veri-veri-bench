def outer():
    def a():
        return b() + 1
    def b():
        return 10
    return a
print(outer()())
