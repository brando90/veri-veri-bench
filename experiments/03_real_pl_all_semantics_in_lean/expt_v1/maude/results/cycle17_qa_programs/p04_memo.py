memo = {}
def ways(n):
    if n in memo:
        return memo[n]
    if n < 2:
        r = 1
    else:
        r = ways(n - 1) + ways(n - 2) + ways(n // 2)
    memo[n] = r
    return r
s = 0
for i in range(60):
    s += ways(i) % 1000
print(s)
print(ways(59) % 100000)
