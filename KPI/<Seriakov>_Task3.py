from math import *
from decimal import Decimal
#'Introduction to programming':Task 3
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 3")
print("Seriakov Vlad, FB-21")
def fact(n): 
    if(n==1 or n==0): 
        return 1 
    else: 
        return n*fact(n-1)

def main():
    i = 0
    while(i == 0):
        try:
            x = Decimal(input('Введіть значення x: ')) 
            z = Decimal(input('Введіть значення z: '))
            y = (x - z / (z - x**2 / 4) - x**2 / fact(5))
            y = y.quantize(Decimal('1.000'))
            print(f'y = {y}')
            i = 1
        except:
            print('Повторіть спробу, ваші данні не підходять під ОДЗ або введено некоректні данні')
            i = 0
main()
