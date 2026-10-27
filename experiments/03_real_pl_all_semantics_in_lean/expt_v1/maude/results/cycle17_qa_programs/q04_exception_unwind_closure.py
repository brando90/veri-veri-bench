saved = []
def inner(k):
    if k == 2:
        raise Exception("boom")
    return k
def middle(k):
    v = k * 7
    saved.append(lambda: v + 1)
    r = inner(k)
    return r
for k in range(4):
    try:
        print(middle(k))
    except Exception as e:
        print("caught")
for f in saved:
    print(f())
