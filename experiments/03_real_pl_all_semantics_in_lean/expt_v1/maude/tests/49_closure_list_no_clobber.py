# a closure's private list is not written back over a same-named caller variable
def make():
    items = []
    def add(v):
        items.append(v)
    return add
add = make()
items = [1, 2, 3]
add(5)
print(len(items))
def run():
    buf = [7, 8, 9]
    add(1)
    return len(buf)
print(run())
