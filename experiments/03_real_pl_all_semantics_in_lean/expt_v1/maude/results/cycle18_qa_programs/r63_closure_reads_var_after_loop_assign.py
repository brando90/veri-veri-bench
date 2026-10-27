def outer():
    fs = []
    for i in range(3):
        fs.append(lambda: total)
        try:
            print(fs[i]())
        except Exception as e:
            print("NE")
        total = i * 10
    return fs[0]()
print(outer())
