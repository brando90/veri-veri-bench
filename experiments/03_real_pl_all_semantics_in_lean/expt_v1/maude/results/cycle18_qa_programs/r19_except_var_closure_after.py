def outer():
    fs = []
    try:
        raise Exception("boom")
    except Exception as e:
        def get():
            return e
        fs.append(get)
        print(get())
    try:
        return fs[0]()
    except Exception as err:
        return "deleted"
print(outer())
