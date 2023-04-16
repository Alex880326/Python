N = int(input('Введите количество элементов: '))
Inputed = input("Введите числа через пробел: ").split()
A = list(map(int, Inputed))
if len(A) != N or N == 0:
    print(f'Введите {N} чисел!')
else:
    X = int(input('Введите число, а программа покажет самый близкий по величине элемент из массива: '))
    min = abs(X - A[0])
    j = 0
    for i in range(1, N):
        count = abs(X - A[i])
        if count < min:
            min = count
            j = i
print(f'Число {X}, близко по величине к числу {A[j]}')