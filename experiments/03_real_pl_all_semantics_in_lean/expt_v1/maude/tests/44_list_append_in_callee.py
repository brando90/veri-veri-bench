# a list mutated inside a callee is visible to the caller
def add(xs, v):
    xs.append(v)
nums = [1, 2]
add(nums, 3)
add(nums, 4)
print(len(nums))
print(nums[3])
def setfirst(ys):
    ys[0] = 42
setfirst(nums)
print(nums[0])
items = []
def push(v):
    items.append(v)
push(10)
push(20)
print(len(items))
print(items[1])
def local_only():
    items = []
    items.append(1)
    items.append(2)
print(len(items))
local_only()
print(len(items))
def rebind(zs):
    zs = [9, 9, 9]
rebind(nums)
print(len(nums))
def outer(ws):
    inner(ws)
def inner(vs):
    vs.append(7)
box = []
outer(box)
print(len(box))
def boom(xs):
    xs.append(5)
    raise Exception(1)
bag = []
try:
    boom(bag)
except Exception as e:
    print(len(bag))
