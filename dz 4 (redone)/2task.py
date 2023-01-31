import random

print("введите n и m")
n = int(input())
m = int(input())
x = [0] * n
for i in range(n):
    x[i] = [0] * m
for i in range(n):
    for v in range(m):
            x[i][v] = random.randint(-1, 10)
print(x)
k = 0
print('введите номер строки и строчки, для завершения введите "11" и "11" ')
i = 0
v = 0
while i != 11:
    i = int(input())
    v = int(input())
    if i == 11:
        break
    elif x[i][v] == -1:
        k = k
        break
    else:
        k += x[i][v]
if k >= 20:
    print("" , k, 'potatoes, task has been completed')
else:
    print("" , k, 'potatoes, task not completed')