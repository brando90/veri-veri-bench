def mk(n):
    st = [n]
    def inc():
        st[0] = st[0] + 1
        return st[0]
    return {'inc': inc, 'st': st}
o = mk(10)
f = o['inc']
f()
f()
print(o['st'][0])
o2 = mk(0)
g = o2['inc']
print(g())
print(o['st'][0])
