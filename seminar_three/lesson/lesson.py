import pandas as pd

print(pd)

print(pd.DataFrame)

print(pd.DataFrame.describe)

dir(pd.DataFrame)


# Полиморфизм - Переопределение
class Parent:
    def execute(self):
        print("Executing a Parent class")


class Child(Parent):
    def execute(self):
        print("Executing a Child class")


# Абстракция
class House:
    def __init__(self, area, geo_position,height):
        self.area = area
        self.geo_position = geo_position
        self.height = height
