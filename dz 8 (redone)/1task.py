from functools import reduce

lissst = [1, -1, -2, 2, -3, 3, 4]
x = list(filter(lambda item: item > 0, lissst))
s = reduce(lambda a,b: a*b, x)
print(s)