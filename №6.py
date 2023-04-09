arr = input("Введите номер билета: ")

if len(arr) != 6:
    print('Введите 6 - ти значный билет')
else:
    sum1 = int(arr[0]) + int(arr[1]) + int(arr[2])
    sum2 = int(arr[3]) + int(arr[4]) + int(arr[5])
    if sum1 == sum2:
        print('Ваш билет счастливый')
    else:
        print('Ваш билет несчастливый')
