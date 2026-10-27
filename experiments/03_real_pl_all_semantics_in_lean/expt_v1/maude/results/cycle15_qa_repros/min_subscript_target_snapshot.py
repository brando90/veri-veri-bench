log = []
def rec(v):
    log.append(v)
    return len(log)
print(log[rec(8) - 1])
