"""""
Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""""

# Создаем список
new_list = [2, 5, 6.7, 8.3, "Dragon", bool, None]

# Определяем тип данных элементов списка
for data_type in new_list:
    print(f"Этот тип данных: {type(data_type)}")