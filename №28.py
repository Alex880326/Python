def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a+1, b-1)
a = int(input("Введите первое число: ")) 
b = int(input("Введите второе число: "))
print("Ответ:",sum(a,b))