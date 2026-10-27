# nested while loops with continue/break at each level
total = 0
a = 0
while a < 3:
    a = a + 1
    if a == 2:
        continue
    b = 0
    while b < 3:
        b = b + 1
        if b == 2:
            continue
        c = 0
        while c < 3:
            c = c + 1
            if c == 2:
                continue
            d = 0
            while d < 3:
                d = d + 1
                if d == 2:
                    continue
                total = total + 1
print(total)
# five levels of for with break/continue
count = 0
for i in range(4):
    if i == 1:
        continue
    for j in range(4):
        if j == 2:
            continue
        for k in range(4):
            if k == 3:
                break
            for l in range(3):
                if l == 1:
                    continue
                for m in range(3):
                    if m == 2:
                        break
                    count = count + 1
print(count)
