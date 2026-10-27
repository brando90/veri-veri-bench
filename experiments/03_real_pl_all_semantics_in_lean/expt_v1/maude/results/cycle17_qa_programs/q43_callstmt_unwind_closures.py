reg = []
def leaf(n):
    if n % 2 == 1:
        raise Exception("odd")
    return n
def mid(n):
    tag = n * 3
    def show():
        return tag + 1000
    reg.append(show)
    leaf(n)
    reg.append(lambda: tag)
def top(n):
    try:
        mid(n)
    except Exception as e:
        reg.append(lambda: n * -1)
for i in range(4):
    top(i)
print(len(reg))
for f in reg:
    print(f())
