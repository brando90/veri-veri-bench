f = lambda x: x
g = lambda x: x + 1
a = {(f, 1): "a", (g, 1): "b"}
b = {(g, 1): "b", (f, 1): "a"}
print(a == b)
