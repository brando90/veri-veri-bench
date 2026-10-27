def mk():
    st = {'n': 0}
    def inc():
        st['n'] = st['n'] + 1
        return st['n']
    def get():
        return st['n']
    return inc, get
inc, get = mk()
inc()
inc()
inc2, get2 = mk()
inc2()
print(get())
print(get2())
