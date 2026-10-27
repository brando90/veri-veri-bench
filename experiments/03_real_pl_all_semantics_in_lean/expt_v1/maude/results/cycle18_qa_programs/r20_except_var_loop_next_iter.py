def f():
    for i in range(3):
        try:
            print(e)
        except Exception as x:
            print("unb")
        try:
            raise Exception(i)
        except Exception as e:
            print(e)
    return 0
print(f())
