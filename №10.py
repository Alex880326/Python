n = int(input('Введите количество монет: '))
eagle = tail = 0
for i in range(n):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        eagle += 1
    else:
        tail += 1
if eagle < tail:
    print(f'Требуется перевернуть {eagle} монет(у)')
elif eagle == tail:
    print('Количество орлов и решек одинаково')
else:
    print(f'Требуется перевернуть {tail} монет(у)')
