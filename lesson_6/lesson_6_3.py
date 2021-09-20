# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:19:25 2021

@author: sheba
"""

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
    name, surname, position (должность), income (доход).
    Последний атрибут должен быть защищенным и ссылаться на словарь,
    содержащий элементы: оклад и премия, например,
    {"wage": wage, "bonus": bonus}.
    Создать класс Position (должность) на базе класса Worker.
    В классе Position реализовать методы получения полного имени сотрудника
    (get_full_name) и дохода с учетом премии (get_total_income).
    Проверить работу примера на реальных данных. Создать экземпляры класса
    Position, передать данные, проверить значения атрибутов,
    вызвать методы экземпляров.
"""

class Worker():
    def __init__(self, name: str, surname: str, position: str,
                 wage: float, bonus: float = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    
    def get_total_income(self):
        return sum(self._income.values())

var = Position("Ivan", "Ivanov", "Employee", 90, 10)
print(var.get_full_name())
print(var.get_total_income())
