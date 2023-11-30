import math


class Rectangle:
    def __init__(self, width, length):
        self.diag = None
        self.perimeter = None
        self.width = width
        self.length = length

    def __add__(self, other):
        return self.area + other.area

    def __eq__(self, other):
        return self.area == other.area

    def calc_area(self):
        self.area = self.length * self.width
        return self.area

    def calc_perimetr(self):
        self.perimeter = 2 * (self.width + self.length)
        return self.perimeter

    def calc_diag_len(self):
        self.diag = (self.width ** 2 + self.length ** 2) ** 0.5
        return self.diag

    def calc_diag_angles(self):
        """Calculates and returns two angles
        between the diagonals in degrees."""

        if not hasattr(self, 'diag'):
            self.calc_diag_len()

        cos_diag_length = self.length / self.diag
        angle_diag_length = math.acos(cos_diag_length)
        angle_diag_length = math.degrees(angle_diag_length)
        first_angle = 180 - (2 * angle_diag_length)
        second_angle = (360 - 2 * first_angle) / 2
        assert first_angle + second_angle == 180
        return first_angle, second_angle


r = Rectangle(1, 2)
r2 = Rectangle(20, 40)
r2.calc_area()
print(r.width, r.length, r.calc_area(), r.calc_perimetr(), r.calc_diag_len(), r.calc_diag_angles())
print(type(r))
print(r + r2, r == r2)

