d = {1: "one", 2: "two", 3: "three"}
print(1 in d)
print(4 in d)
print(d[2])

# integer keys mixed with use in functions
def lookup(table, k):
    if k in table:
        return table[k]
    return "missing"

print(lookup(d, 1))
print(lookup(d, 3))
print(lookup(d, 99))

# build a frequency table
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
freq = {}
for w in words:
    if w in freq:
        freq[w] = freq[w] + 1
    else:
        freq[w] = 1
print(freq["apple"])
print(freq["banana"])
print(freq["cherry"])
