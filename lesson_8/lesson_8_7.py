# -*- coding: utf-8 -*-
"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных
экземпляров. Проверьте корректность полученного результата.
"""

class ComplexNumber:
    def __init__(self, re, im, *args):
        self.re = re
        self.im = im

    def __add__(self, other):
        return ComplexNumber((self.re + other.re), (self.im + other.im))

    def __mul__(self, other):
        return ComplexNumber((self.re * other.re - (self.im * other.im)),\
                             (self.re * other.im + self.im * other.re))

    def __str__(self):
        return f'z = {self.re} + {self.im}i'


z1 = ComplexNumber(1, 2)
z2 = ComplexNumber(3, -4)
print(z1)
print(z2)
print(f"z1 + z2 = {z1 + z2}")
print(f"z1 * z2 = {z1 * z2}")
