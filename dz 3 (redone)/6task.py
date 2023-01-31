n = int(input())
x = float(input())
k = 0
b = 1
for i in range(n + 1):
    if i > 0:
        b *= i
        k += (b * (x**i))
print(k)