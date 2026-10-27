xs = [1, 2, 3]
calls = []
def bad():
    calls.append("bad")
    raise Exception("idx")
def rhs():
    calls.append("rhs")
    return 1
try:
    xs[bad()] += rhs()
except Exception as e:
    print(e)
print(calls)
print(xs)
