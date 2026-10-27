def make(n):
    total = n * 10
    def get():
        return total + n
    def add(k):
        return total + k
    return {"g": get, "a": add}
fs = []
i = 0
while i < 4:
    fs.append(make(i))
    i += 1
for d in fs:
    print(d["g"]())
    print(d["a"](1))
