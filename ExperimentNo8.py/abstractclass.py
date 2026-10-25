from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    def display(self):
        print("This is a vehicle")

class Car(Vehicle):

    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):

    def start(self):
        print("Bike starts with a self-start button")

bike = Bike()
car = Car()
car.display()
car.start()

print()

bike.display()
bike.start()