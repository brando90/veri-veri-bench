def shrink(a):
    a *= 0
    return 1
xs = [1, 2, 3]
try:
    xs[2] += shrink(xs)
except Exception as e:
    print("IE")
print(xs)
