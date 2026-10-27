def l3(n):
    t = n + 1
    if t > 3:
        raise Exception("deep")
    return t
def l2(n):
    s = n * 2
    return l3(s) + s
def l1(n):
    r = 0
    try:
        r = l2(n)
    except Exception as e:
        r = -1
    return r * 10 + n
for i in range(4):
    print(l1(i))
x = 5
print(x)
