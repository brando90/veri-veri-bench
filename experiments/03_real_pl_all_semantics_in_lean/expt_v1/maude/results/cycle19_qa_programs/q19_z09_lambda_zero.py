ops = {"div": lambda a, b: a // b, "mod": lambda a, b: a % b}
res = []
for name in ["div", "mod"]:
    for b in [3, 0, -2]:
        try:
            res.append(ops[name](7, b))
        except Exception as e:
            res.append(name)
print(res)
