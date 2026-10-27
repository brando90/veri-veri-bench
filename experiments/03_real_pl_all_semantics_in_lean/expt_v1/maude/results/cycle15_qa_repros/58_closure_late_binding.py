# a closure reads the variable's value at call time, not at def time
def mk():
    x = 1
    def get():
        return x
    x = 2
    return get
print(mk()())
def mk2():
    def get():
        return y
    y = 5
    return get
print(mk2()())
def loopfs():
    fs = []
    for i in range(3):
        def f():
            return i
        fs.append(f)
    return fs
fs = loopfs()
print(fs[0]() + fs[1]() + fs[2]())
