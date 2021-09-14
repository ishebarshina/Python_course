# -*- coding: utf-8 -*-

# 1. Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений
# необходимо запускать скрипт с параметрами.

from sys import argv

script_name, working_hours, rate_hour, bonus = argv


def calc_salary(working_hours, rate_hour, bonus):
    try:
        salary = (float(working_hours) * float(rate_hour)) + float(bonus)
        print("salary = {}".format(salary))
    except ValueError:
        print("Параметры введены некорректно")


calc_salary(working_hours, rate_hour, bonus)

