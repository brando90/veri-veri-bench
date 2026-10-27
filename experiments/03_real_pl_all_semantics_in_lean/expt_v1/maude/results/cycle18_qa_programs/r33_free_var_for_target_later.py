i = 100
def outer():
    def peek():
        return i
    try:
        a = peek()
    except Exception as e:
        a = -1
    for i in range(3):
        pass
    return a + peek()
print(outer())
