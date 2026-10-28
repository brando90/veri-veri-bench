pairs = [("ab", "abc"), ("abc", "ab"), ("", "a"), ("a", ""), ("", ""), ("a", "a")]
for p in pairs:
    a, b = p
    print((a < b, a <= b, a > b, a >= b))
