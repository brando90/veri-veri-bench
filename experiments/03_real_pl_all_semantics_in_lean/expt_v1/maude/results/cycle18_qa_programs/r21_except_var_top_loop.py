for i in range(3):
    try:
        print(err)
    except Exception as z:
        print("ne")
    try:
        raise Exception(i * 10)
    except Exception as err:
        print(err)
