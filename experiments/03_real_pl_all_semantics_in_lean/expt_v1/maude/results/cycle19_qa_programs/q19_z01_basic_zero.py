for a in [1, 0, -5, 7]:
    try:
        print(a // 0)
    except Exception as e:
        print("fd")
    try:
        print(a % 0)
    except Exception as e:
        print("md")
try:
    print(3 + (4 // 0) * 2)
except Exception as e:
    print("expr")
try:
    print(10 % (3 - 3))
except Exception as e:
    print("expr2")
print(7 // 2)
print(-7 % 3)
