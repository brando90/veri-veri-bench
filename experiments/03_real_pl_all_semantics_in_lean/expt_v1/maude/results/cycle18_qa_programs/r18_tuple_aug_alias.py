t = (1, 2)
alias = t
t += (3,)
print(alias)
print(t)
t *= 2
print(t)
print(alias)
def f(x):
    x += (4,)
    return x
print(f(alias))
print(alias)
