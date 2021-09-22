# -*- coding: utf-8 -*-

"""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра.
"""


class Stationery():
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f"I'm drawing with a pen {self.title}.")


class Pencil(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f"I'm drawing with a pencil {self.title}.")


class Handle(Stationery):
    def __init__(self, title: str):
        super().__init__(title)

    def draw(self):
        print(f"I'm drawing with a handle {self.title}.")


obj = Stationery("any stationery")
obj.draw()

obj = Pen("Pilot")
obj.draw()

obj = Pencil("Derwent")
obj.draw()

obj = Handle("Arteza")
obj.draw()


