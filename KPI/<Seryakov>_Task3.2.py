#'Introduction to programming':Task 3
#Smirnova Natalia, FB-21, V-1(21)

from math import *
class ComplexNumber:
    def __init__(self, r, i, other_r, other_i):
        self.r = r
        self.i = i
        self.other_r = other_r
        self.other_i = other_i
    def __str__(self):
        if self.i < 0:
            return f"{self.r - abs(self.i)}i"
        else:
            return f"{self.r + self.i}i"
    def __plus__(self):
        return ComplexNumber(self.r + self.other_r, self.i + self.other_i)
    def __minus__(self):
        return ComplexNumber(self.r - self.other_r, self.i - self.other_i)
    def __multiply__(self):
        return ComplexNumber(self.r * self.other_r - self.i * self.other_i,
                       self.i * self.other_r + self.r * self.other_i)
    def __divide__(self):
        a = self.other_r ** 2 + self.other_i ** 2
        return ComplexNumber((self.r * self.other_r + self.i * self.other_i) / a,
                       (self.i * self.other_r - self.r * self.other_i) / a)
    def __abs__(self):
        return sqrt(self.r ** 2 + self.i ** 2)