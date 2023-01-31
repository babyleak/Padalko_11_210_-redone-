import re

x = input()
y = input()
result = len(re.findall(x, y))
print(result)