def setter():
    return 3
try:
    raise Exception(1)
except Exception as val:
    pass
def use():
    return val
try:
    use()
except Exception as e:
    print("ne")
val = setter()
print(use())
