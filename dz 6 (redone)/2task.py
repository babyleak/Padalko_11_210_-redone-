import random as r

x = ["Алим",
    "Мансур",
    "Фарида",
    "Роман",
    "Анна",
    "Владимир",
    "Татьяна",
    "Вера",
    "Елизавета",
    "Ольга",
    "Елена",
    "Екатерина",
    "Виктор",
    "Юрий",
    "Борис",
    "Евгений",
    "Валентин",
    "Валентина",
    "Нина",
    "Мария",
    "Светлана",
    "Владислав",
    "Богдан",
    "Алеся",
    "Оксана",
    "Виталий",
    "Милана",
    "Трофим",
    "Ярослав",
    "Серафим",
    "Олег",
    "Юрий",
    "Руслан",]

s1 = set(r.choices(x, k=20))
while len(s1) < 20:
    s1.add(r.choice(x))
s2 = set(r.choices(x, k=20))
while len(s2) < 20:
    s2.add(r.choice(x))
s3 = set(r.choices(x, k=20))
while len(s3) < 20:
    s3.add(r.choice(x))

print("Списки групп:")
print(f"Первая группа ({len(s1)} человек):", *s1)
print(f"Вторая группа ({len(s2)} человек):", *s2)
print(f"Третья группа ({len(s3)} человек):", *s3)
print()

oneofthis = s1.difference(s2, s3)
oneofthis.update(s2.difference(s1, s3))
oneofthis.update(s3.difference(s2, s3))
teski = s1.intersection(s2, s3)

print("список тезок:", *teski, sep="\n")
print()
print("список людей без тезок в других группах:", *oneofthis, sep="\n")