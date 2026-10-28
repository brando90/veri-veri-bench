words = ["ant", "bee", "cat", "catfish", "dog", "eel", "emu"]
def find(w):
    lo = 0
    hi = len(words) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if words[mid] == w:
            return mid
        if words[mid] < w:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
for w in ["cat", "catfish", "ca", "emu", "zzz", "", "dog"]:
    print(find(w))
