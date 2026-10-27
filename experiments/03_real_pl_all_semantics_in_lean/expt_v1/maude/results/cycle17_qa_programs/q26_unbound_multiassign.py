a = 1
b = 2
def swap():
    a, b = b, a
    return a
try:
    print(swap())
except Exception as e:
    print("ule")
def swap2(a, b):
    a, b = b, a
    return a * 10 + b
print(swap2(1, 2))
