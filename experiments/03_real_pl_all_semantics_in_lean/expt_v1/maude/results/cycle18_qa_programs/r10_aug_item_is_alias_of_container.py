xs = [1, 2]
holder = [xs, xs]
holder[0] += holder[1]
print(xs)
print(len(holder[1]))
holder[1] *= 2
print(len(xs))
print(xs[7])
