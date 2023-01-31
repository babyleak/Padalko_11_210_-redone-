t = int(input())
a = []
while t > 0:
    s = input()
    a.append(s)
    t -= 1
for i in range(len(a)):
    print(a[i].strip('0').count('0'))