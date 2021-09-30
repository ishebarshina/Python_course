# -*- coding: utf-8 -*-
"""
3. Создайте собственный класс-исключение, который должен проверять содержимое
списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""

import sys

class OwnError(Exception):
    def __init__(self):
        print("Для завершения введите stop")
        self.elem = input("Введите следующий элемент списка: ")
        self.res_list = []
        while (self.elem != 'stop'):
            try:
                self.elem = float(self.elem)
            except ValueError:
                pass
            else:
                self.res_list.append(self.elem)
            self.elem = input("Введите следующий элемент списка: ")
        print(f"resulting list: {self.res_list}")

x = OwnError()