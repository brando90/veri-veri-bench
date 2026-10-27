xs = [1, 2, 3, 4, 5]
total = 0
for i in range(1, len(xs) + 1):
    total = total * 10 + xs[-i]
print(total)
for i in range(1, 4):
    xs[-i] = xs[-i] * 100
print(xs)
stack = [1]
while len(stack) < 6:
    stack.append(stack[-1] * 2)
print(stack)
