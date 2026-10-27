def f(flag):
    if flag:
        try:
            raise Exception("r")
        except Exception as e:
            pass
    else:
        e = "assigned"
    try:
        return e if flag else e + "!"
    except Exception as z:
        return "unb"
print(f(True))
print(f(False))
