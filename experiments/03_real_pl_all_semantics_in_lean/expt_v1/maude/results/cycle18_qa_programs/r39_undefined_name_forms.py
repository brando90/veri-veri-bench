out = []
try:
    print(nothere)
except Exception as e:
    out.append(1)
try:
    nofunc(1)
except Exception as e:
    out.append(2)
try:
    x = len(nolist)
except Exception as e:
    out.append(3)
try:
    nolist2.append(1)
except Exception as e:
    out.append(4)
try:
    nolist3[0] = 1
except Exception as e:
    out.append(5)
try:
    nolist4[0] += 1
except Exception as e:
    out.append(6)
try:
    nocount += 1
except Exception as e:
    out.append(7)
try:
    for z in nolist5:
        pass
except Exception as e:
    out.append(8)
print(out)
