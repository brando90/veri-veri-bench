# assignments made before a raise are visible in the handler
x = 1
try:
    x = 2
    y = 10
    raise Exception(7)
    x = 99
except Exception as e:
    print(x)
    print(y)
    print(e)
# raise inside a loop keeps the loop's progress
i = 0
try:
    while i < 10:
        i = i + 1
        if i == 4:
            raise Exception(i)
except Exception as e:
    print(i)
    print(e)
# raise escaping from a function call statement
def boom(n):
    raise Exception(n + 1)
k = 0
try:
    k = 5
    boom(k)
    k = 100
except Exception as e:
    print(k)
    print(e)
# nested try: inner handler state flows outward
a = 0
try:
    try:
        a = 1
        raise Exception(3)
    except Exception as e:
        a = a + 1
        raise Exception(a)
except Exception as e2:
    print(a)
    print(e2)
