t0 = ()
t1 = (5,)
t = (1, (2, 3), "x")
for tt in [t0, t1, t]:
    n = len(tt)
    for i in [n - 1, n, -n, -n - 1]:
        try:
            print(tt[i])
        except Exception as e:
            print("IE")
try:
    print(t[1][2])
except Exception as e:
    print("nested")
print(t[1][-2])
try:
    print(t[2][1])
except Exception as e:
    print("str")
