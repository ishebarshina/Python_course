# -*- coding: utf-8 -*-
"""
4. Начните работу над проектом «Склад оргтехники».
Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа
оргтехники.
5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и
количестве единиц оргтехники, а также других данных, можно использовать любую
подходящую структуру, например словарь.
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации
вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
"""


class OfficeEquipment:
    def __init__(self, name):
        self.name = name
        self.current_status = "working"

    @property
    def status(self):
        print(f"Current status: {self.current_status}")

    def update_status(self, new_status):
        self.current_status = new_status


class Printer(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)
        self.paint = 0

    @property
    def paint_available(self):
        print(f"Amount of paint in printer: {self.paint} % ")

    def update_paint_percent(self, new_paint):
        try:
            self.paint = float(new_paint)
            if (self.paint < 0 or self.paint > 100):
                raise ValueError
        except ValueError:
            print("Incorrect input.")
            pass
        else:
            print(f"Paint updated: {self.paint} %")


class Scanner(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)
        self.__max_memory = 1028
        self.memory = self.__max_memory

    @property
    def max_memory(self):
        print(f"max_memory = {self.__max_memory}")

    def add_doc(self, size):
        if (size <= self.memory):
            self.memory -= size
            print(f"Document is added, free memory: {self.memory}")
        else:
            print(f"Not enough memory.")

    def del_doc(self, size):
        if ((size + self.memory) < self.__max_memory):
            self.memory -= size
        else:
            print("Incorrect input")

    def show_memory(self):
        print(f"{self.memory} from {self.__max_memory} available.")


class Copier(OfficeEquipment):
    def __init__(self, name):
        super().__init__(name)
        self.paper = 0

    @property
    def paper_available(self):
        print(f"Amount of paper in printer: {self.paper} sheets ")

    def update_paper(self, new_paper):
        try:
            self.paper = int(new_paper)
        except ValueError:
            print("Incorrect input.")
            pass
        else:
            print(f"Updated amount of paper: {self.paper} sheets")

# %%

class Warehouse:
    """Класс, описывающий склад."""
    def __init__(self, name):
        self.name = name
        self.copiers_in_stock = {}
        self.scanners_in_stock = {}
        self.printers_in_stock = {}


    def add_item(self, *args):
        for obj in args:
            if type(obj) is Copier:
                try:
                    self.copiers_in_stock[obj.name].append(obj)
                except KeyError:
                    self.copiers_in_stock[obj.name] = [obj]
            elif type(obj) is Scanner:
                try:
                    self.scanners_in_stock[obj.name].append(obj)
                except KeyError:
                    self.scanners_in_stock[obj.name] = [obj]
            elif type(obj) is Printer:
                try:
                    self.printers_in_stock[obj.name].append(obj)
                except KeyError:
                    self.printers_in_stock[obj.name] = [obj]
            else:
                print("Incorrect argument")

    @staticmethod
    def __find_sum(dictionary):
        return sum([len(dictionary[i]) for i in list(dictionary.keys())])

    def number_printers(self):
        print(f"Amount of printers in warehouse: {self.__find_sum(self.printers_in_stock)}")

    def number_scanners(self):
        print(f"Amount of scanners in warehouse: {self.__find_sum(self.scanners_in_stock)}")

    def number_copiers(self):
        print(f"Amount of copiers in warehouse: {self.__find_sum(self.copiers_in_stock)}")


# %% пример работы кода

print1 = Printer("print1")
print1.paint_available
print1.status
print1.update_status("сломан")
print1.status
print1.update_paint_percent(200)
print1.paint_available
print1.update_paint_percent(20)
print1.paint_available
print2 = Printer("print2")
print3 = Printer("print1")

# %%

scanner1 = Scanner("scanner1")
scanner1.max_memory
scanner1.status
scanner1.add_doc(10)
scanner1.show_memory()
scanner1.del_doc(100)
scanner1.show_memory()

# %%

copier1 = Copier("copier1")
copier1.status
copier1.update_status("doesn't work")
copier1.status
copier1.paper_available
copier1.update_paper(10.1)
copier1.paper_available
copier1.update_paper('d')
copier1.paper_available

# %%

warehouse1 = Warehouse("warehouse1")
warehouse1.add_item(print1, print2, print3, scanner1, copier1)

# %%

warehouse1.number_copiers()
warehouse1.number_printers()
warehouse1.number_scanners()
