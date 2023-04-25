def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a*a, b//2)
    else:
        return a * power(a, b-1)
    
a = int(input("Введите число возводимое в степень: ")) 
b = int(input("Введите степень: "))
print("Ответ:",power(a,b))