d = {(1, 2): 3}
print(d[(1, 2)])
for k in [(2, 1), (1,), (1, 2, 3), ()]:
    try:
        print(d[k])
    except Exception as e:
        print("KE")
