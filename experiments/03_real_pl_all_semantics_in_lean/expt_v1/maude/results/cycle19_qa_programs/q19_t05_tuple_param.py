def f(t):
    try:
        t[0] += ["x"]
    except Exception as e:
        print("TE")
    return t
lst = []
r = f((lst,))
print(r)
print(lst)
