x = 17
try:
    x //= 0
except Exception as e:
    print("a")
print(x)
try:
    x %= 0
except Exception as e:
    print("b")
print(x)
x //= 5
print(x)
x %= 2
print(x)
y = 0
try:
    y %= y
except Exception as e:
    print("c")
print(y)
