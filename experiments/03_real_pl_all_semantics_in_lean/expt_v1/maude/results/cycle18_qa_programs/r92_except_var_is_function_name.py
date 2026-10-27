def helper():
    return "h"
try:
    raise Exception("x")
except Exception as helper:
    print(helper)
try:
    print(helper())
except Exception as z:
    print("helper gone")
