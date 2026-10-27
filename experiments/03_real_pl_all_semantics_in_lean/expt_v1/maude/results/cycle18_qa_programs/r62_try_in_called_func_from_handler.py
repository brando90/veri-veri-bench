def helper():
    try:
        raise Exception("h")
    except Exception as e:
        print(e)
        return "h!"
def f():
    try:
        raise Exception("f")
    except Exception as e:
        r = helper() + "f"
        print(e)
    try:
        print(e)
        return "still"
    except Exception as z:
        return r
print(f())
