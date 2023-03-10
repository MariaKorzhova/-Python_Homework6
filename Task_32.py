# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7] 
# Вывод: [1, 9, 13, 14, 19]

Count_elem1 = int(input("Введите количество элементов списка: "))
Min_elem = int(input("Введите минимальное число диапазона: "))
Max_elem = int(input("Введите максимальное число диапазона: "))

lst1 = []
for i in range(Count_elem1):
        lst1.append(int(input("Введите элемент списка: ")))
print(lst1)

def Index (lst1, Min_elem, Max_elem):
    lst2 = []
    for i in range(len(lst1)):
        if Min_elem <= lst1[i] <= Max_elem:
            lst2.append(lst1[i])
            print(i, end=' ')

Index (lst1, Min_elem, Max_elem)
