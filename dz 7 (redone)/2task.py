import re

fNames = ["ова[., \n]", "ева[., \n]", "ина[., \n]", "ына[., \n]", "ская[., \n]", "цкая[., \n]", ]

MNames = ["ов[., \n]", "ев[., \n]", "ин[., \n]", "ын[., \n]", "ский[., \n]", "цкий[., \n]", ]

n = input()

female_results = 0
male_results = 0

for i in range(len(fNames)):
    female_results += len(re.findall(fNames[i], n, flags=re.M))
for i in range(len(MNames)):
    male_results += len(re.findall(MNames[i], n, flags=re.M))
print(f"женщин: {female_results}")
print(f"мужчин: {male_results}")