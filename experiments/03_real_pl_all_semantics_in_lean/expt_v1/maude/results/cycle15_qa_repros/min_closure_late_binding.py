def mk():
    x = 1
    def get():
        return x
    x = 2
    return get
print(mk()())
