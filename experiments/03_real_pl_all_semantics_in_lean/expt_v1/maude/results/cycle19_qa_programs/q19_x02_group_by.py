words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]
g = {}
for w in words:
    k = w[0]
    try:
        g[k] += [w]
    except Exception as e:
        g[k] = [w]
print(g)
h = {"c": ["cherry"], "b": ["banana", "blueberry"], "a": ["apple", "avocado", "apricot"]}
print(g == h)
