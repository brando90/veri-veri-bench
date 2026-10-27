log = []
def base_i(i):
    log.append("i" + str_of(i))
    return i
def str_of(i):
    return "0" if i == 0 else ("1" if i == 1 else "x")
def rhs(v):
    log.append("r")
    return v
xs = [1, 2]
xs[base_i(1)] += rhs(5)
print(xs)
print(log)
