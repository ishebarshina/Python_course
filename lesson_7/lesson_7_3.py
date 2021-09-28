# -*- coding: utf-8 -*-
"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
Данные методы должны применяться только к клеткам и выполнять увеличение,
уменьшение, умножение и целочисленное (с округлением до целого) деление клеток,
соответственно.
"""


class Cell:
    """Класс Клетка."""

    def __init__(self, num: int):
        """Check if num is int."""
        if (type(num) == int and num > 0):
            self.num = num
        else:
            raise TypeError("Кол-во ячеек должно быть целым")

    def __add__(self, obj):
        """Override addition method."""
        return Cell(self.num + obj.num)

    def __sub__(self, obj):
        """Override subtraction operator."""
        if (obj.num < self.num):
            return Cell(round(self.num - obj.num))
        else:
            raise ValueError("The cell has fewer nucleus.")

    def __mul__(self, obj):
        """Override multiplication method."""
        return Cell(self.num * obj.num)

    def __truediv__(self, obj):
        """Override division method."""
        return Cell(self.num // obj.num)

    def  make_order(self, row):
        """Organise cell in rows."""
        n = self.num // row
        m = self.num % row
        res = ''
        for i in range(n):
            res += ''.join('*' for i in range(row)) + '\n'
        res += ''.join('*' for i in range(m))
        return res

# %%

x = Cell(5)
y = Cell(3)
print(f"Cell(5) + Cell(3) = Cell({(x+y).num})")
print(f"Cell(5) - Cell(3) = Cell({(x-y).num})")
print(f"Cell(5) * Cell(3) = Cell({(x*y).num})")
print(f"Cell(5) / Cell(3) = Cell({(x/y).num})")
x = Cell(12)
print(x.make_order(5))
