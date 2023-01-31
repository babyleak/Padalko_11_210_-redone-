x = input()
y = input()
b = float(x)
a = float(y)
s = int(input())
if abs(b) < abs(s) and abs(a) < abs(s):
    print('попадает')
else:
    print('не попадает')