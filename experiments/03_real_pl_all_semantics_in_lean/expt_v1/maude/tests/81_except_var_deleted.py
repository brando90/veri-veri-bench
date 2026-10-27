# the except-as variable is deleted when the handler ends
def f():
    try:
        raise Exception("x")
    except Exception as e:
        got = e
    try:
        return e
    except Exception as e2:
        return "gone"
print(f())
def g():
    e = "before"
    try:
        raise Exception("y")
    except Exception as e:
        pass
    try:
        print(e)
    except Exception as e2:
        print("deleted")
g()
def h():
    for i in range(3):
        try:
            raise Exception(i)
        except Exception as err:
            if i == 1:
                continue
            print(err)
    try:
        return err
    except Exception as e3:
        return -1
print(h())
def k():
    try:
        raise Exception("a")
    except Exception as ex:
        return ex
print(k())
try:
    raise Exception("t")
except Exception as top:
    pass
try:
    print(top)
except Exception as t2:
    print("top gone")
def m():
    try:
        raise Exception(1)
    except Exception as e:
        try:
            raise Exception(2)
        except Exception as e:
            pass
        try:
            return e
        except Exception as e9:
            return "inner gone"
print(m())
