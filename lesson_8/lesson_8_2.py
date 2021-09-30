# -*- coding: utf-8 -*-
"""
2. Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):

    @staticmethod
    def division(num, denom):
        try:
            res = num / denom
        except ZeroDivisionError:
            print("Division by zero exception.")
        else:
            print(f"{num} / {denom} = {res}")


OwnError.division(1, 0)

# %% другой вариант 

import sys

class OwnError(Exception):
    def __init__(self):
        try:
            self.num = float(input("Числитель: "))
            self.denom = float(input("Знаменатель: "))
        except Exception:
            print("Incorrect input")
            sys.exit()

    @property
    def division(self):
        try:
            self.res = self.num / self.denom
        except ZeroDivisionError:
            print("Division by zero exception.")
        else:
            print(f"{self.num} / {self.denom} = {self.res}")


x = OwnError()
x.division
