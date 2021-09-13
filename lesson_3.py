# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 21:19:49 2021

@author: iShebarshina
"""

# %%

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.


def division(x, y):
    if y != 0:
        return x/y
    else:
        print("Деление на ноль")

# %%

# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_profile(name, surname, year, city, email, phone):
    print(f"{name} {surname}, {year}, {city}, {email}, {phone}")


user_profile(name="Ivan", surname="Ivanov", city="Moscow", phone="4645",
             year="1956", email="mail@mail")

# %%

# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(arg1, arg2, arg3):
    s = [arg1, arg2, arg3]
    s.sort(reverse=True)
    return s[0] + s[1]


print(my_func(3, 6, 5))

# %%

# 4. Программа принимает действительное положительное число x
# и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись
# без встроенной функции возведения числа в степень.
# ** Подсказка:** попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.


def my_func_41(x, y):
    if(type(y) != int):
        print("Incorrect type")
        return ''
    if(x < 0 or y > 0):
        print("x < 0 or y > 0")
        return ''
    return x ** y


print(my_func_41(5.0, -2))


def my_func_42(x, y):
    if(type(y) != int):
        print("Incorrect type")
        return ''
    if(x < 0 or y > 0):
        print("x < 0 or y > 0")
        return ''
    b = -y
    s = x
    for i in range(b-1):
        s = s * s
    return 1/s


print(my_func_42(5, -2))

# %%

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ,
# выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

# Решение реализовано так, что выход происходит при вводе любого
# не числового символа, за исключением пробела и точки
# (для возможности работать с типом float)


def my_func5():
    s = 0
    while(True):
        in_str = str(input())
        try:
            li_str = in_str.split(' ')
            if (li_str[-1] == ''):
                li_str.remove('')
            li = list(map(lambda x: float(x), li_str))
            s = s + sum(li)
            print(f"s = {s}")
        except ValueError:
            in_str_tup = tuple(in_str)
            i = 0
            while(47 < ord(in_str_tup[i]) < 58 or
                  in_str_tup[i] == ' ' or
                  in_str_tup[i] == '.'):
                i = i + 1
            if (i > 0):
                in_str_part = ''
                for x in in_str_tup[:i]:
                    in_str_part = in_str_part + x
                li_str_part = in_str_part.split(' ')
                if(li_str_part[-1] == ''):
                    li_str_part.remove('')
                li = list(map(lambda x: float(x), li_str_part))
                s = s + sum(li)
            print(f"s = {s}")
            print("Non-numeric symbol")
            return


my_func5()

# Example:
# Input: 1 2 3 4.4
# Output: s = 10.4
# Input: 1 2 3 4 f 4
# Output: s = 20.4
#         Non-numeric symbol

# %%

# 6. Реализовать функцию int_func(), принимающую слово
# из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием.
# В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться
# с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func().


def int_func_0(word):
    if(word.islower()):
        return word[0].upper() + word[1:]
    else:
        print("Enter a word in lower register")
        return


print(int_func_0("word"))


def int_func_1(in_str):
    li_str = in_str.split(' ')
    if((all(list(map(lambda x: x.islower(), li_str)))) == False):
        print("Enter every word in lower register")
        return ''
    new_str = ''
    for elem in li_str:
        new_str = new_str + int_func_0(elem) + ' '
    return new_str[:-1]


print(int_func_1("better late than never"))
