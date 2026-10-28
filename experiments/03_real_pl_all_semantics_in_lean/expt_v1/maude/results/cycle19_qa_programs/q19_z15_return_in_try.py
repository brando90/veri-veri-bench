def safe(a, b):
    try:
        return a // b
    except Exception as e:
        return -999
res = []
for b in [2, 0, -3, 0]:
    res.append(safe(9, b))
print(res)
def safe2(a, b):
    while True:
        try:
            return a % b
        except Exception as e:
            b = b + 1
print(safe2(9, 0))
