# range with a negative literal step counts down
for i in range(5, 0, -2):
    print(i)

# an exception raised inside a loop body is caught outside the loop
n = 0
try:
    while True:
        n = n + 1
        if n == 3:
            raise Exception("stop")
except Exception as e:
    print("caught")
print("after")

# continue / break in a while with an else-free nested if chain
k = 0
acc = 0
while k < 20:
    k = k + 1
    if k % 2 == 0:
        continue
    elif k > 9:
        break
    else:
        acc = acc + k
print(acc)
print(k)
