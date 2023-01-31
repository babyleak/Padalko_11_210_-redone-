n = int(input())
a = 0
b = 1
c = 1
while b <= n:
    c *= b
    a += c
    b += 1
print(a)