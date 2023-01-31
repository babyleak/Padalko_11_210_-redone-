import random

a = 0
b = 0
c = 0
n = 0
s = []
x = "not q"
h = 0
m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
while x != "q":
    h += 1
    print('статистика:', c, "%/", n, "%")
    print('загаданные числа:', s)
    print('какое число от 0 до 9 загадано сейчас ? , q - закончить')
    r = random.randint(0, 9)
    x = input()
    if int(x) in m:
        s.append(r)
        if int(x) == r:
            a += 1
        else:
            b += 1
        c = int((a * 100)/h)
        n = 100 - c
    else:
        x = input()