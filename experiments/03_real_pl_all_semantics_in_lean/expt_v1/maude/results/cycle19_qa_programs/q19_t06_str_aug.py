s = "ab"
try:
    s[0] += "x"
except Exception as e:
    print("TE")
try:
    s[5] += "x"
except Exception as e:
    print("IE")
print(s)
s += "c"
print(s)
