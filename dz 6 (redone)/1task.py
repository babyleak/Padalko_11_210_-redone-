x = '1'
while x != 'quit':
    x = input()
    if x == 'quit':
        break
    x = '1' + x
    s = ''
    for i in range(len(x)):
        if x[i] != x[i-1]:
            s += x[i]
        else:
            y = 1
            s += str(y)
    print(s[1:])