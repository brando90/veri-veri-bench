def f():
    for e in range(3):
        try:
            raise Exception(e * 2)
        except Exception as e:
            print(e)
    try:
        return e
    except Exception as z:
        return "loop var deleted"
print(f())
