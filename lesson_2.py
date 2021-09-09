# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 21:19:49 2021

@author: carmine
"""

# %%
# 1. Создать список и заполнить его элементами различных типов данных.
# В данном списке представлены следующие типы данных:
# int, float, str, list, bool, tuple
var_list_1 = [1, 1.0, 'common_str', [1, 2, 3], bool(0), tuple([1, 2, 3])]
# Реализовать скрипт проверки типа данных каждого элемента.
for i in var_list_1:
    print(type(i))
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# %%

# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

from ast import literal_eval


def recognise(elem):
    try:
        return literal_eval(elem)
    except (ValueError, SyntaxError):
        return str(elem)


var_list_2 = []
a = input()
while(a != 'quit'):
    var_list_2.append(recognise(a))
    a = input()

print("Initial list:")
for elem in var_list_2:
    print(f"element: {elem} \t type: {type(elem)}")

i = 0
while i < len(var_list_2) - 1:
    var_list_2[i], var_list_2[i+1] = var_list_2[i+1], var_list_2[i]
    i = i + 2

print("After swapping elements:")
for elem in var_list_2:
    print(f"element: {elem} \t type: {type(elem)}")

# %%

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

n_month = int(input("Введите целое число от 1 до 12: "))

# via list
if (n_month in [1, 2, 12]):
    print("Winter")
elif (n_month in [3, 4, 5]):
    print("Spring")
elif (n_month in [6, 7, 8]):
    print("Summer")
elif (n_month in [9, 10, 11]):
    print("Autumn")
else:
    print("Incorrect number of month")

# via dict
month_dict = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5],
              'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}

if (n_month in month_dict['Winter']):
    print("Winter")
elif (n_month in month_dict['Spring']):
    print("Spring")
elif (n_month in month_dict['Summer']):
    print("Summer")
elif (n_month in month_dict['Autumn']):
    print("Autumn")
else:
    print("Incorrect number of month")

# %%

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

in_str = str(input("Enter string: "))
# in_str = 'fgh ghj kl hnm yui 0123456789456'
pr_str = in_str.split(' ')
print("Номер строки: строка")
for i in range(len(pr_str)):
    print(f"{i}: {pr_str[i][:10]}")

# %%

# 5. Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

rating_list = [7, 5, 3, 3, 2]
for i in range(3):
    new_elem = int(input("Введите новый элемент рейтинга: "))
    rating_list.append(new_elem)
    rating_list.sort(reverse=True)
    print(f"Рейтинг: {rating_list}")

# %%

# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик,
# например список названий товаров.

products = []
for i in range(3):
    name = str(input("Название: "))
    price = float(input("Цена: "))
    amount = int(input("Количество, штук: "))
    products.append(tuple([i, {"Название": name, "Цена": price,
                               "Количество": amount, "ед": "шт."}]))

# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]

products_keys = list(products[0][1].keys())
analytics = {}
for k in range(len(products_keys)):
    analytics.update({products_keys[k]: []})
for i in range(len(products)):
    for k in range(len(products_keys)):
            analytics[products_keys[k]].append(products[i][1][products_keys[k]])

print("Analitics:")
for i in analytics:
    print(f"{i}: {analytics[i]}")







