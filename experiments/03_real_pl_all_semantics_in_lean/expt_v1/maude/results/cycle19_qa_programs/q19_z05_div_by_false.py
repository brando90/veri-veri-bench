try:
    print(7 // False)
except Exception as e:
    print("f1")
try:
    print(7 % (True - True))
except Exception as e:
    print("f2")
print(7 // True)
print(7 % True)
print(True // True)
print(False // True)
b = False
try:
    b //= b
except Exception as e:
    print("f3")
print(b)
