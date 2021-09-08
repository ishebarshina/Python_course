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

# var_list_2 = list(input(""))
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


