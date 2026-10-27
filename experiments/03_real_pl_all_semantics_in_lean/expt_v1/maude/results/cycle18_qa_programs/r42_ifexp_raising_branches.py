def boom(m):
    raise Exception(m)
def pick(c):
    return boom("t") if c else "safe"
print(pick(False))
try:
    print(pick(True))
except Exception as e:
    print(e)
def cond():
    raise Exception("cond")
try:
    v = 1 if cond() else 2
except Exception as e:
    print(e)
calls = []
def mark(v):
    calls.append(v)
    return v
r = mark(1) if mark(0) else mark(2)
print(r)
print(calls)
