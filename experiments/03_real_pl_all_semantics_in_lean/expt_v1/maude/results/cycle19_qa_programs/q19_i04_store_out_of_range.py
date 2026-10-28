def setit(a, i, v):
    try:
        a[i] = v
        return True
    except Exception as e:
        return False
xs = [1, 2, 3]
r = []
for i in [3, -4, 2, -3, 100, -100]:
    r.append(setit(xs, i, i * 10))
print(r)
print(xs)
def mk():
    ys = [0]
    def put(i):
        try:
            ys[i] = 9
        except Exception as e:
            return "no"
        return ys
    return put
put = mk()
print(put(1))
print(put(-1))
print(put(-2))
