e = [1]
def f():
    try:
        raise Exception(5)
    except Exception as e:
        return e
print(f())
print(len(e))
