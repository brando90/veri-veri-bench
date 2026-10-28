try:
    try:
        x = [1][5]
    except Exception as e:
        print("inner")
        y = 1 // 0
        print("not here")
except Exception as e2:
    print("outer")
print("done")
