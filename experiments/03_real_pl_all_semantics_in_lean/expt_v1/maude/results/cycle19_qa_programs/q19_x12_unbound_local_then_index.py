def f():
    try:
        print(xs[0])
    except Exception as e:
        print("unbound")
    xs = [1]
    try:
        print(xs[1])
    except Exception as e:
        print("IE")
    return xs
print(f())
