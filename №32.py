import random
lst = [random.randint(0, 22) for i in range(10)]
min_val = int(input("Минимальное значение: "))
max_val = int(input("Максимальное значение: "))
res = []

for i in range(len(lst)):
    if min_val <= lst[i] <= max_val:
        res.append(i)
        
print(f"Случайно сгенерированный массив чисел: {lst}")
if res:
    print(f"Индексы элементов, значения которых принадлежат заданному диапазону {res}")
else:
    print("В списке нет элементов, которые принадлежали бы заданному диапазону.")