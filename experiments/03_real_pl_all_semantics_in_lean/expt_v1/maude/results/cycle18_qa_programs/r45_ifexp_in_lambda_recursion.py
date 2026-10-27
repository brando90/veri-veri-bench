def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)
print(fact(10))
fib = lambda n: n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(12))
def collatz(n):
    return 0 if n == 1 else 1 + collatz(n // 2 if n % 2 == 0 else 3 * n + 1)
print(collatz(27))
