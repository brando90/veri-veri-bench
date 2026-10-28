def f():
    try:
        x = 1 // 0
    except Exception as e:
        print("h")
    try:
        print(e)
    except Exception as e2:
        print("unbound")
    return 1
print(f())
try:
    q = 2 % 0
except Exception as err:
    print("h2")
try:
    print(err)
except Exception as e3:
    print("name")
