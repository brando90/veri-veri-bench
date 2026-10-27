def f():
    try:
        try:
            raise Exception("a")
        except Exception as e:
            raise Exception("ab")
    except Exception as e:
        print(e)
    try:
        print(e)
    except Exception as q:
        print("gone")
f()
try:
    try:
        raise Exception(1)
    except Exception as e:
        raise Exception(2)
except Exception as e:
    print(e)
try:
    print(e)
except Exception as q:
    print("top gone")
