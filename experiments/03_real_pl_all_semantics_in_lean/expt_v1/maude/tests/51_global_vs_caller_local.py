# a helper reads the global of its name, not the same-named local of its caller
x = 1
def helper():
    return x
def caller():
    x = 2
    return helper()
print(caller())
print(helper())
def caller2(x):
    return helper() + x
print(caller2(10))
def deep():
    x = 5
    def mid():
        return helper()
    return mid()
print(deep())
y = 7
def usey():
    return y + 1
def setter():
    y = 100
    z = usey()
    return z + y
print(setter())
y = 8
print(setter())
