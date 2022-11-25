from math import *
#'Introduction to programming':Task 4
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 4")
print("Seriakov Vlad, FB-21")
sum = 0.0
n = 1
while (10**n/factorial(n) > 0.0001):
    sum = (10**n/factorial(n)) + sum
    n += 1
print(round(sum, 4))