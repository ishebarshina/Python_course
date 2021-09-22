# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:35:07 2021

@author: sheba
"""

"""
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты:
    speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction), которые должны сообщать,
    что машина поехала, остановилась, повернула (куда).

Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.

Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля.

Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    speed: float
    color: str
    name: str
    is_police: bool

    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False

    def go(self, speed):
        self.speed = speed
        print(f"{self.color} {self.name} car started moving.")

    def stop(self):
        self.speed = 0
        print(f"{self.color} {self.name} car stoped.")

    def turn(self, direction: str):
        print(f"The car turned {direction}")

    def show_speed(self):
        print(f"Car speed is {self.speed} km/h")


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        super().show_speed()
        if (self.speed > 60):
            print("Overspeed warning: reduce your speed")


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)

    def show_speed(self):
        super().show_speed()
        if (self.speed > 40):
            print("Overspeed warning: reduce your speed")


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True


obj = Car("Nissan", "black")
obj.go(60)
obj.turn("left")
obj.show_speed()
obj.stop()
obj.show_speed()

obj = TownCar("Ford", "grey")
obj.go(50)
obj.turn("left")
obj.show_speed()
obj.stop()
obj.show_speed()

obj = TownCar("Mercedes", "dark blue")
obj.go(80)
obj.turn("left")
obj.show_speed()
obj.stop()
obj.show_speed()

obj = SportCar("Toyota Supra", "yellow")
obj.go(120)
obj.turn("right")
obj.show_speed()
obj.stop()
obj.show_speed()

obj = WorkCar("Kia", "white")
obj.go(60)
obj.turn("right")
obj.show_speed()
obj.stop()
obj.show_speed()

obj = PoliceCar("Volvo", "blue")
obj.go(60)
obj.turn("right")
obj.show_speed()
obj.stop()
obj.show_speed()