# -*- coding: utf-8 -*-
"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, str_date: str):
        self.str_date = str_date
            
    @classmethod
    def cast_date(cls, str_date):
        date = str_date.split('-')
        try:
            day = int(date[0])
            month = int(date[1])
            year = int(date[2])
        except ValueError:
            print("Incorrect input. Can't cast into int.")
        else:
            return day, month, year
        
    @staticmethod
    def valid_date(date):
        day = date[0]
        month = date[1]
        year = date[2]
        try:
            if (year <= 0):
                raise ValueError
        except:
            print("year < 0")
        try:
            if (month <= 0 or month > 12):
                raise ValueError
        except:
            print("month <= 0 or month > 12")
        try:
            if (day <= 0 or day > 31):
                raise ValueError("day <= 0 or day > 31")
        except ValueError:
            print("day <= 0 or day > 31")
        else:
            return f"Date is ok"


x = Date("12-12-1234d")
d, m, y = Date.cast_date("12-12-1234")
print(d, m, y)
print(Date.valid_date(Date.cast_date("12-12-1234")))
print(Date.cast_date("12-12-1234d"))
print(Date.valid_date(Date.cast_date("12-13-1234")))
            
            
        