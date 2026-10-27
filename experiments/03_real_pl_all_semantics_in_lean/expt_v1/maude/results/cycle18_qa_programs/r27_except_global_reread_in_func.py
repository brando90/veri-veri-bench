err = "g"
def reader():
    return err
try:
    raise Exception("x")
except Exception as err:
    print(reader())
try:
    print(reader())
except Exception as q:
    print("NameError in reader")
err = "back"
print(reader())
