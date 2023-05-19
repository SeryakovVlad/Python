#'Introduction to programming':Task 3
#Seriakov Vlad, FB-21, V-2(22)

from math import *
class ComplexNumber:
    def __init__(self, r, phi):
        self.r = r
        self.phi = phi
    def __str__(self):
        return str(self.r * cos(self.phi)), str(self.r * sin(self.phi))
    def __plus__(self, other_r, other_phi):
        x = self.r * cos(self.phi) + other_r * cos(other_phi)
        y = self.r * sin(self.phi) + other_r * sin(other_phi)
        r = sqrt(x**2 + y**2)
        phi = atan2(y, x)
        return ComplexNumber(r, phi)
    def __minus__(self, other_r, other_phi):
        x = self.r * cos(self.phi) - other_r * cos(other_phi)
        y = self.r * sin(self.phi) - other_r * sin(other_phi)
        r = sqrt(x**2 + y**2)
        phi = atan2(y, x)
        return ComplexNumber(r, phi)
    def __multiply__(self, other_r, other_phi):
        r = self.r * other_r
        phi = self.phi + other_phi
        return ComplexNumber(r, phi)
    def __divide__(self, other_r, other_phi):
        r = self.r / other_r
        phi = self.phi - other_phi
        return ComplexNumber(r, phi)
    def __abs__(self):
        return abs(self.r)