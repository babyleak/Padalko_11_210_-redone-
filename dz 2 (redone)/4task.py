x = input()
y = input()
b = float(x)
a = float(y)
s = 0
if (b**2 + a**2) < 10**2:
    k = b**2 + a**2
    while s < 100:
        if k < s**2:
            print(s)
            break
        else:
            s += 1
else:
    print('не попал')