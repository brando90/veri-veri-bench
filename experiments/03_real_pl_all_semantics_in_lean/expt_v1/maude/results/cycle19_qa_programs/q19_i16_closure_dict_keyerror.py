def mk():
    d = {}
    def get(k):
        try:
            return d[k]
        except Exception as e:
            d[k] = len(d)
            return -1
    return get, d
get, d = mk()
print(get("a"))
print(get("b"))
print(get("a"))
alias = d
alias["c"] = 99
print(get("c"))
print(d)
