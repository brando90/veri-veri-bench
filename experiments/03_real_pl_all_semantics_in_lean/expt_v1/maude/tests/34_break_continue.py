# break in while
i = 0
while True:
    if i == 5:
        break
    i = i + 1
print(i)

# continue in while (increment first)
n = 0
odd_sum = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    odd_sum = odd_sum + n
print(odd_sum)

# break / continue in for-range
total = 0
for k in range(100):
    if k % 3 == 0:
        continue
    if k > 10:
        break
    total = total + k
print(total)

# for over list, nested loops: break only leaves the inner loop
found = 0
for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        if b > a:
            break
        found = found + 1
print(found)

# break inside try, state is kept
j = 0
while j < 10:
    try:
        j = j + 1
        if j == 4:
            break
    except e:
        print(99)
print(j)

# continue inside try inside for
c = 0
for q in range(6):
    try:
        if q == 2:
            continue
        c = c + q
    except e:
        print(99)
print(c)

# break inside a function's loop, then return
def first_over(xs, lim):
    r = -1
    for v in xs:
        if v > lim:
            r = v
            break
    return r
print(first_over([3, 8, 12, 20], 10))
print(first_over([1, 2], 10))
