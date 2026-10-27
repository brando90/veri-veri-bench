def outer():
    e = "outer-e"
    def inner():
        try:
            raise Exception("inner")
        except Exception as e:
            print(e)
            return "r"
    r = inner()
    return r + "/" + e
print(outer())
