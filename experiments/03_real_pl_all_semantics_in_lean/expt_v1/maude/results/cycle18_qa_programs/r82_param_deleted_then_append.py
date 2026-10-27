err = ["global"]
def f(err):
    try:
        raise Exception("x")
    except Exception as err:
        pass
    try:
        err.append(1)
    except Exception as z:
        return "unbound"
    return "appended"
print(f([0]))
print(err)
