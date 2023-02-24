from random import randint
n=int(input('Введите количество человек: '))
a=[randint(140, 220) for i in range(n)]
print(a)
summ=0
for i in range(n):
 summ+=a[i]
print('Средний рост =',summ/n)