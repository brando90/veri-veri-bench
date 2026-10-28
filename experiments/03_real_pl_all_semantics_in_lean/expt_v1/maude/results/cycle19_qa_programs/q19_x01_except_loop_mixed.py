data = [[1, 2], {"a": 1}, (5,), "s", [0]]
keys = [5, "b", 3, 9, 0]
out = []
for i in range(len(data)):
    try:
        out.append(data[i][keys[i]])
    except Exception as e:
        out.append("E")
print(out)
try:
    print(e)
except Exception as e:
    print("gone")
