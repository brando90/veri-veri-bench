def f():
    i = 0
    while True:
        i += 1
        try:
            raise Exception(i)
        except Exception as e:
            if i < 3:
                continue
            print(e)
            break
    try:
        print(e)
    except Exception as x:
        print("gone")
    return i
print(f())
