# -*- coding: utf-8 -*-
"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа
оргтехники.
"""


class OfficeEquipment:
    def __init__(self, name):
        self.name = name
        self.status = "working"

    @property
    def status(self):
        print("Current status: {self.status}")

    def update_status(self):
        self.status = input("Enter current status: ")


class Printer(OfficeEquipment):
    def __init__(self, name):
        super().__init__(self, name)
        self.paint = 0

    @property
    def paint_available(self):
        print("Amount of paint in printer: {self.paint} % ")

    @property
    def update_paint(self):
        try:
            self.paint = input("Input percent of paint: ")
            if (self.paint < 0 or self.paint > 100):
                raise ValueError
        except ValueError:
            print("Incorrect input.")
            pass
        else:
            print("Paint updated: {self.paint} %")


class Scanner(OfficeEquipment):
    def __init__(self, name):
        super().__init__(self, name)
        self.__max_memory = 1028
        self.memory = self.__max_memory

    def add_doc(self, size):
        if (size <= self.memory):
            self.memory -= size
            print("Document is added, free memory: {self.memory}")
        else:
            print("Not enough memory.")

    def del_doc(self, size):
        if ((size + self.memory) < self.__max_memory):
            self.memory -= size
        else:
            print("Incorrect input")

    def show_memory(self):
        print("{self.memory} from {self.__max_memory} available.")


class Copier(OfficeEquipment):
    def __init__(self, name):
        super().__init__(self, name)
        self.paper = 0

    @property
    def paper_available(self):
        print("Amount of paper in printer: {self.paper} sheets ")

    @property
    def update_paper(self):
        try:
            self.paper = int(input("Update amount of paper: "))
        except ValueError:
            print("Incorrect input.")
            pass
        else:
            print("Updated amount of paper: {self.paper} sheets")


class Warehouse:
    """Класс, описывающий склад.
    Композиция."""
