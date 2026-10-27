c = 5
def outer():
    def read():
        return c
    try:
        print(read())
    except Exception as e:
        print("NE1")
    c = 0
    c += 7
    return read()
print(outer())
