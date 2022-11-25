from math import *
from decimal import Decimal
#'Introduction to programming':Task 2
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 2")
print("Seriakov Vlad, FB-21")
print('Вирішити цей приклад: (15-x/y)/(33**y+19.3)+z')

def main():
    i = 0
    while(i == 0):
         try:
            x = Decimal(input('Введіть значення x: ')) 
            y = Decimal(input('Введіть значення y: '))
            z = Decimal(input('Введіть значення z: '))
            r = ((15 - x/y)/(33**y + Decimal(19.3)) + z)
            r = r.quantize(Decimal('1.000'))
            print(r)
            i = 1
         except:
            print('Повторіть спробу, ваші данні не підходять під ОДЗ або введено некоректні данні')
            i = 0
main()