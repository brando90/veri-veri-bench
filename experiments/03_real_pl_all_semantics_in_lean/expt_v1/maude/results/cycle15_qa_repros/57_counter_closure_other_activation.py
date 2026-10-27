# a closure that mutates its own list, called repeatedly from a different activation
def counter():
    count = []
    def inc():
        count.append(1)
        return len(count)
    return inc
c = counter()
print(c())
print(c())
print(c() + c())
def use():
    return c() * 10 + c()
print(use())
