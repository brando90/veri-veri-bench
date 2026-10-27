memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n < 2:
        r = n
    else:
        r = fib(n - 1) + fib(n - 2)
    memo[n] = r
    return r
print(fib(25))
print(len(memo))
