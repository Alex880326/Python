from random import randint
list_1 = list(randint(1, 5) for i in range(int(input('Введите кол-во кустов: '))))
print(list_1)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
    res = list_1[-2] + list_1[-1] + list_1[0]
else:
    res = list_1[a-1] + list_1[a-2] + list_1[a]
print(res, 'ягод')