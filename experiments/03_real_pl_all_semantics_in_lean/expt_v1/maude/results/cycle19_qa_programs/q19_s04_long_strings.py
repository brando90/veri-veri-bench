a = "abcdefghijklmnopqrstuvwxyz" * 4
b = a + "a"
c = "abcdefghijklmnopqrstuvwxyz" * 3 + "abcdefghijklmnopqrstuvwxyA"
print(a < b)
print(b < a)
print(c < a)
print(a <= a)
print(c >= a)
m = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
n = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
print(m < n)
print(m > n)
