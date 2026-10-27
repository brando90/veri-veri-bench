y = 1
def outer():
    def inner():
        return y
    try:
        r = inner()
    except Exception as e:
        r = 55
    y = 2
    return r
print(outer())
