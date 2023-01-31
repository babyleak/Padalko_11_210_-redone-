s = input()
b = s[::-1]
x = list(b)
a = 0
for i in range(len(b)):
    if x[i] == '1':
        a += 2**i
print(a)