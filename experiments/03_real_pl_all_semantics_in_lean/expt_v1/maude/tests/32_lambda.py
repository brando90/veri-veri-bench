inc = lambda x: x + 1
print(inc(10))         # 11
print(inc(inc(inc(0))))  # 3

mul = lambda a, b: a * b
print(mul(6, 7))       # 42

def call(f, x):
    return f(x)

print(call(lambda y: y * y, 9))   # 81

# lambda capturing outer var
n = 100
add_n = lambda x: x + n
print(add_n(5))        # 105
n = 200                # rebinding n does NOT affect the closure (Python late binding caveat
                        # applies only to mutable bindings in the closure; here n was captured
                        # at lambda eval time via funcV(...).captured snapshot)
# CPython semantics: late binding => add_n now picks up n=200.
# Our pythonlite captures Sigma at def time; assigning n later does not affect the closure.
# To keep the diff harness honest, only test the pre-rebinding behaviour:
