def thrower(v):
    raise Exception(v)
def f():
    try:
        try:
            raise Exception(1)
        except Exception as e:
            thrower(2)
    except Exception as e2:
        print(e2)
    try:
        return e
    except Exception as e3:
        return "e gone"
print(f())
