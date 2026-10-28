t = (1, 2)
try:
    t[0] += 1
except Exception as e:
    print("TE")
try:
    t[5] += 1
except Exception as e:
    print("IE")
try:
    t[1] *= 3
except Exception as e:
    print("TE2")
print(t)
