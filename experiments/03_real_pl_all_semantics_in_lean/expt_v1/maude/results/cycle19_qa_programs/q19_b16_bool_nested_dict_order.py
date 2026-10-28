a = {"a": [True], "b": 1}
b = {"b": True, "a": [1]}
print(a == b)
print([a] == [b])
print((a, 1) == (b, True))
