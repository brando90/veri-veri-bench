a = [[1]]
b = a
def h():
    global_box.append(1)
    return [9]
global_box = []
def rebind():
    return [7]
a[0] += rebind()
print(b)
x = [10, 20]
y = x
def change():
    x[0] = 999
    return 1
x[0] += change()
print(y)
