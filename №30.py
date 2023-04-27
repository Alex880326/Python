a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progr = []
for i in range(n):
    progr.append(a1 + i * d)

print(progr)