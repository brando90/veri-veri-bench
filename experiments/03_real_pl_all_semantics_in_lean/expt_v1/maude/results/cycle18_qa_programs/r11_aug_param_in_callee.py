def add_to(lst, extra):
    lst += extra
    return len(lst)
a = [1]
print(add_to(a, [2, 3]))
print(a)
def add_tup(t, extra):
    t += extra
    return t
u = (1, 2)
print(add_tup(u, (3,)))
print(u)
def mul_box(box, i):
    box[i] *= 2
    return box[i]
bx = [[1], "ab", 3]
print(mul_box(bx, 0))
print(mul_box(bx, 1))
print(mul_box(bx, 2))
print(bx)
