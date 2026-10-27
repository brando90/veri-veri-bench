# a closure mutating an enclosing local, called from a sibling closure
def outer():
    xs = []
    def add(v):
        xs.append(v)
        return len(xs)
    def twice(v):
        add(v)
        return add(v)
    r = twice(1)
    print(r)
    print(len(xs))
    return len(xs) + twice(2)
print(outer())
