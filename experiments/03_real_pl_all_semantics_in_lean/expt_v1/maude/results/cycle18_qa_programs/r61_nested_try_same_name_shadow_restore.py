def f():
    e = "orig"
    try:
        raise Exception("first")
    except Exception as e:
        try:
            raise Exception("second")
        except Exception as e:
            print(e)
        try:
            print(e)
        except Exception as z:
            print("inner deleted")
    try:
        print(e)
    except Exception as z:
        print("outer deleted")
    return 0
print(f())
