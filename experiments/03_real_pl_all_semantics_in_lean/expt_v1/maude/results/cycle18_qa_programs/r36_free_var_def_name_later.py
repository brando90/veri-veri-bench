def helper():
    return "global helper"
def outer():
    def caller():
        return helper()
    try:
        r = caller()
    except Exception as e:
        r = "NE"
    def helper():
        return "local helper"
    return r + "|" + caller()
print(outer())
