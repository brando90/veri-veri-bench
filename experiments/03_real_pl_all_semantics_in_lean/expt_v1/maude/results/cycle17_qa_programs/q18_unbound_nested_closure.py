def outer():
    q = 5
    def inner():
        a = q
        q = 6
        return a
    try:
        return inner()
    except Exception as e:
        return 42
print(outer())
