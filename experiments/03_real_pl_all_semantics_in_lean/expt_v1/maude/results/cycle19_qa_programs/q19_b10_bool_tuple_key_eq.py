d = {}
d[(True, False)] = "x"
print(d[(1, 0)])
d[(1, 0)] = "y"
print(d)
print({(True,): 1} == {(1,): 1})
print({(1, (True,)): 2} == {(True, (1,)): 2})
