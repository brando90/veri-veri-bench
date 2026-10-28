def count(s):
    c = {}
    for ch in s:
        try:
            c[ch] += 1
        except Exception as e:
            c[ch] = 1
    return c
print(count("abracadabra"))
print(count("abracadabra") == count("aaaaabbrrcd"))
print(count("abc") == count("abd"))
