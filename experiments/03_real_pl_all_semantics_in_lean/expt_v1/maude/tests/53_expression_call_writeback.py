# list mutation in a callee is visible to the caller when the call is in expression position
def add(xs):
    xs.append(9)
    return len(xs)
nums = [1, 2]
n = add(nums)
print(n)
print(len(nums))
print(add(nums))
print(len(nums))
print(add(nums) + add(nums))
print(len(nums))
def setfirst(ys, v):
    ys[0] = v
    return v + 1
k = setfirst(nums, 42) * 2
print(k)
print(nums[0])
def run():
    local = [5]
    m = add(local)
    return m * 10 + len(local)
print(run())
store = []
def push(v):
    store.append(v)
    return len(store)
a = push(3)
b = push(4)
print(a + b)
print(len(store))
if push(1) > 2:
    print(len(store))
def wrap(zs):
    r = add(zs)
    return r
t = []
print(wrap(t))
print(len(t))
r = [add(t), add(t)]
print(len(t))
