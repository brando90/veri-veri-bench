xs = [1, 2, 3]
def g():
    return [9][3]
def p():
    print("rhs")
    return 1
try:
    xs[g()] += p()
except Exception as e:
    print("caught")
print(xs)
