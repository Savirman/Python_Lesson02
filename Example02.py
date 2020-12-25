"""""
Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы
с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

# Создание списка элементов, вводимых пользователем
first_list = []

len_of_list = int(input("Задайте длину списка: "))
index = 0
while index < len_of_list:
    element = input("Введите элемент списка: ")
    first_list.append(element)
    index = index + 1

print(first_list[:])

# Создание списка элементов из списка элементов, введенных пользователем, путем перестановки соседних элементов
new_list = []

if len_of_list % 2 == 0:
    i = 0
    while i <  len_of_list:
        new_list.extend(first_list[i + 1])
        new_list.extend(first_list[i])
        i = i + 2
    print(new_list[:])
else:
    i = 0
    while i < len_of_list - 1:
        new_list.extend(first_list[i + 1])
        new_list.extend(first_list[i])
        i = i + 2
    new_list.append(first_list[len_of_list - 1])

    print(new_list[:])