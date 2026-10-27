y = "global"
def gp():
    def parent():
        def child():
            return y
        return child()
    try:
        r = parent()
    except Exception as e:
        r = "NameError"
    y = "gp"
    return r + "," + parent()
print(gp())
