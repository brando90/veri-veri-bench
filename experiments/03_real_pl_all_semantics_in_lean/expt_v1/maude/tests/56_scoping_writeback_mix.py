# scoping and write-back together
total = []
def log(v):
    total.append(v)
    return len(total)
def worker():
    total = [100]
    n = log(1)
    total.append(n)
    return len(total)
print(worker())
print(len(total))
def make():
    seen = []
    def note(v):
        seen.append(v)
        return len(seen)
    def count():
        return len(seen)
    note(1)
    note(2)
    return count()
print(make())
def outer():
    buf = []
    def inner(v):
        buf.append(v)
        return len(buf)
    r = inner(1) + inner(2)
    return r * 10 + len(buf)
print(outer())
d = {}
def setd(k):
    d[k] = 1
    return len(d)
def user():
    d = {"only": 1}
    r = setd("g")
    return r * 10 + len(d)
print(user())
print(len(d))
