def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)
def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)
c = 0
for i in range(20):
    if is_even(i):
        c += 1
print(c)
print(is_odd(41))
