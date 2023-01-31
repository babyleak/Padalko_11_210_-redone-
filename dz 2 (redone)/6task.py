x = int(input())
y = 0
while x > 0:
    y += x % 10
    x = x - x % 10
    x = x / 10
print(y)