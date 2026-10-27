def mk():
    fs = []
    for i in range(2):
        try:
            raise Exception(i)
        except Exception as e:
            fs.append(lambda: e)
            print(fs[i]())
    out = []
    for g in fs:
        try:
            out.append(g())
        except Exception as z:
            out.append("NE")
    return out
print(mk())
