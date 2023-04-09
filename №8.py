width = int(input("Введите количество долек (в длину): "))
height = int(input("Введите количество долек (в ширину): "))
cut = int(input("Введите количество отломленных долек : "))

if width * height >= cut and (cut % width == 0 or cut % height == 0):
    print ("Деление исполнимо")
else:
    print ("Деление невозможно")
