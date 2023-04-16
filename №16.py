N = int(input('Введите количество элементов: '))
A = input("Введите число: ")
list_1 = list(map(int, A))
if len(list_1) != N:
    print(f'Введите {N} чисел!')
else:
    X = int(input('Искомое число: '))
    count = 0
    for i in range(N):
        if list_1[i] == X:
            count += 1
    print(f'Число {X} встречается {count} раз')