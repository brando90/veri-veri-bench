a = [[1, 2]]
alias = a[0]
def boom():
    raise Exception("rhs")
try:
    a[0] += boom()
except Exception as e:
    print(e)
print(alias)
print(a)
try:
    a[0] *= boom()
except Exception as e:
    print(e)
print(len(a[0]))
