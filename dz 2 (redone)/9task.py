s = int(input())
a = []
while s > 0:
    x = s % 2
    a.append(x)
    s = s // 2
    if s == 1:
        a.append(s)
        break
a.reverse()
print("".join(map(str, a)))