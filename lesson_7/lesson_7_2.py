# -*- coding: utf-8 -*-
"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
    реализовать абстрактные классы для основных классов проекта,
    проверить на практике работу декоратора @property.
"""

from abc import ABCMeta, abstractmethod

class Clothes(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, param):
        raise NotImplementedError("Необходимо переопределить метод __init__")

    @abstractmethod
    def fabric_expence(self):
        raise NotImplementedError("Необходимо переопределить метод fabric_expence")

    @staticmethod
    def total_fabric_expence(*argv):
        total = 0
        for obj in argv:
            total = total + obj.fabric_expence
        return total


class Coat(Clothes):
    def __init__(self, name, param):
        self.name = name
        self.V = param

    @property
    def fabric_expence(self):
        return (self.V / 6.5 + 0.5)


class Suit(Clothes):
    def __init__(self, name, param):
        self.name = name
        self.H = param

    @property
    def fabric_expence(self):
        return (2 * self.H + 0.3)
    


# %%

coat1 = Coat("Coat1", 6.5)
coat2 = Coat("Coat2", 13)
coat3 = Coat("Coat3", 19.5)
suit1 = Suit("Suit1", 1)
suit2 = Suit("Suit2", 2)
suit3 = Suit("Suit3", 3)
print(coat1.fabric_expence)
print(coat2.fabric_expence)
print(coat3.fabric_expence)
print(coat1.fabric_expence + coat2.fabric_expence + coat3.fabric_expence)
print(Clothes.total_fabric_expence(coat1, coat2, coat3))
print(Clothes.total_fabric_expence(coat1, coat2, coat3))
print(suit1.fabric_expence)
print(suit2.fabric_expence)
print(suit3.fabric_expence)
print(suit1.fabric_expence + coat2.fabric_expence)
print(Clothes.total_fabric_expence(suit1, coat2))


