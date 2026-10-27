def f(items):
    acc = {"ok": [], "bad": 0}
    for it in items:
        try:
            if it < 0:
                raise Exception(it)
            acc["ok"] += [it]
        except Exception as e:
            acc["bad"] += it
            continue
        acc["ok"] *= 1
    return acc
print(f([1, -2, 3, -4, 5]))
