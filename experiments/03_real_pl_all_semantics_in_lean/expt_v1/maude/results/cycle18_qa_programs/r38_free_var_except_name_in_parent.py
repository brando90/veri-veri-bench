e = "glob"
def outer():
    def read():
        return e
    try:
        before = read()
    except Exception as z:
        before = "NE-before"
    try:
        raise Exception("caught")
    except Exception as e:
        print(read())
    try:
        after = read()
    except Exception as z:
        after = "NE-after"
    return [before, after]
print(outer())
