# list += any iterable (list.extend): tuple, string, dict keys, itself
xs = [1]
xs += (2, 3)
print(len(xs))
print(xs[2])
ys = ["a"]
ys += "bc"
print(len(ys))
print(ys[2])
d = {"p": 1, "q": 2}
ks = []
ks += d
print(len(ks))
print(ks[1])
zs = [1, 2]
zs += zs
print(len(zs))
print(zs[3])
al = [1]
other = al
al += [2]
al += (3,)
al += ""
print(len(other))
def ext(buf):
    buf += "xy"
buf = [0]
ext(buf)
print(len(buf))
print(buf[2])
ws = [[1]]
ws += ((2,),)
print(len(ws))
print(ws[1][0])
