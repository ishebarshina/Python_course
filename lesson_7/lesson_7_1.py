# -*- coding: utf-8 -*-
"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
"""


class Matrix:
    """Class Matrix."""

    def __init__(self, list_data: list):
        """Override constructor."""
        self.matrix = list_data

    def __str__(self):
        """Override method to print matrix."""
        return '\n'.join('\t'.join(str(elem) for elem in line)
                         for line in self.matrix)

    def __add__(self, obj):
        """Override method for addition. Returns Matrix object."""
        matrix2 = []
        for i in range(len(obj.matrix)):
            temp = []
            for j in range(len(obj.matrix[i])):
                temp.append(obj.matrix[i][j] + self.matrix[i][j])
            matrix2.append(temp)
        return Matrix(matrix2)


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8, 9], [0, 1, 2]]
x = Matrix(a)
y = Matrix(b)
print(x.__str__())
print(x.matrix)
print(x)
print(x+y)
