n = int(input())
a = 0
b = 1
c = 0
while c < n:
    b *= n
    a += b
    c += 1
print(a)