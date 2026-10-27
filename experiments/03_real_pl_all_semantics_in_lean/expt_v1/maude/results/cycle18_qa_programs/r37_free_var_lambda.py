k = 3
def outer():
    f = lambda: k * 2
    try:
        a = f()
    except Exception as e:
        a = -1
    k = 4
    return [a, f()]
print(outer())
