t = (1, 2, 3)
try:
    t[0] = 5
except Exception as e:
    print("TE")
try:
    t[-1] = 5
except Exception as e:
    print("TE2")
try:
    t[9] = 5
except Exception as e:
    print("TE3")
print(t)
s = "abc"
try:
    s[0] = "x"
except Exception as e:
    print("TE4")
print(s)
