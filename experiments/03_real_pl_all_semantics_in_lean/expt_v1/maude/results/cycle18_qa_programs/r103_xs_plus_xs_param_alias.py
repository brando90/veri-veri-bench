def dbl(xs):
    xs += xs
    xs[-1] += 100
    return xs
a = [1, 2]
b = dbl(a)
print(a)
print(b)
def dbl_item(box):
    box[0] += box[0]
    return box
c = [[1], [2]]
k = c[0]
dbl_item(c)
dbl_item(c)
print(k)
print(c)
