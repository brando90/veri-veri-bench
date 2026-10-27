def mk2():
    def get():
        return y
    y = 5
    return get
print(mk2()())
