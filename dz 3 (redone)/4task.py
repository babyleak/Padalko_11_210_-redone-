n = int(input())
a = 0
while n > 0:
    b = 2**n
    a += b
    n -= 1
print(a)