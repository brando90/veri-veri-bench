xs = []
def f(xs):
    try:
        raise Exception(1)
    except Exception as xs:
        pass
    xs.append(1)
try:
    f([0])
except Exception as z:
    print("UnboundLocalError")
print(len(xs))
