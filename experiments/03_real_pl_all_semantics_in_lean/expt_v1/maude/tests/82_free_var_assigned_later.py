# a closure reading a variable that its enclosing function assigns only later does not see the global
y = 1
def outer():
    def inner():
        return y
    try:
        r = inner()
    except Exception as e:
        r = 55
    y = 2
    return r + inner()
print(outer())
z = 10
def outer2():
    def inner():
        return z
    z = 20
    return inner()
print(outer2())
w = 5
def outer3(flag):
    def inner():
        return w
    if flag:
        w = 6
    try:
        return inner()
    except Exception as e:
        return -1
print(outer3(True))
print(outer3(False))
def never():
    try:
        return undefined_name
    except Exception as e:
        return "NameError"
print(never())
def reader():
    return glob_later
try:
    reader()
except Exception as e:
    print("not yet")
glob_later = 3
print(reader())
def outer4():
    acc = []
    def push():
        acc.append(len(acc))
    push()
    push()
    return len(acc)
print(outer4())
def outer5():
    def inner():
        late.append(1)
    try:
        inner()
    except Exception as e:
        print("late unbound")
    late = []
    inner()
    return len(late)
print(outer5())
