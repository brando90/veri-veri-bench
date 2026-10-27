# += / *= on a list mutate it in place, so aliases see the change
a = [1]
b = a
b += [2]
print(len(a))
print(a == b)
a += a
print(len(a))
print(a[2] + a[3])
c = [0]
d = c
c *= 3
print(len(d))
# a plain rebinding does not touch the alias
e = [1]
f = e
e = e + [2]
print(len(f))
# in a function: the parameter list is changed for the caller
def grow(xs):
    xs += [9, 9]
    return len(xs)
g = [1]
print(grow(g))
print(g[2])
print(len(g))
# numbers and strings still rebind
n = 5
n += 2
n *= 3
print(n)
s = "ab"
s += "cd"
s *= 2
print(s)
# the right side is evaluated after the left name is read
def pushback(xs):
    xs.append(7)
    return [1]
h = [0]
h += pushback(h)
print(h[1])
print(len(h))
