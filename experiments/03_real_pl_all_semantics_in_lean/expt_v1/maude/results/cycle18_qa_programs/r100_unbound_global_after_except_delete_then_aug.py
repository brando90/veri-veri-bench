total = 0
try:
    raise Exception(5)
except Exception as total:
    pass
try:
    total += 1
except Exception as e:
    print("NE on aug")
total = 10
total += 1
print(total)
