# -*- coding: utf-8 -*-
"""
1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
"""


class Matrix:
    """Class Matrix."""

    def __init__(self, list_data: list):
        self.matrix = list_data

    def get_matrix(self):
        return self.matrix
    
    def __str__(self):
        # return str('\n'.join(['\t'.join([str(j) for j in i]) for i in self.matrix]))
        return "here"



# %%

x = Matrix([[1, 2, 3], [4, 5, 6]])
print(x.__str__())
print(x.matrix)
print(x)