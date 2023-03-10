# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: a n = a1 + (n-1) * d. 
# Каждое число вводится с новой строки.
# Ввод: 7 2 5 
# Вывод: 7 9 11 13 15

First_elem = int(input("Введите первый элемент прогрессии: "))
Differ = int(input("Введите разность между элементами прогрессии: "))
Count_elem = int(input("Введите количество элементов прогрессии: "))

def Progression (First_elem, Differ, Count_elem):
    lst = []
    for i in range(Count_elem):
        lst.append(First_elem+i*Differ)
    print(lst)

Progression (First_elem, Differ, Count_elem)
