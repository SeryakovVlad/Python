from decimal import Decimal
#'Introduction to programming':Task 7.1
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 7.1")
print("Seriakov Vlad, FB-21")
def fact(n):
    if(n==1 or n==0): 
        return 1 
    else: 
        return n*fact(n-1)
while True:
    x = Decimal(input("x:"))
    z = Decimal(input("z:"))
    if(z == (x**2)/4):
        print("Не підходить під ОДЗ")
        continue
    y = x - z / (z - ((x**2)/4)) - x**2/fact(9)
    y = y.quantize(Decimal('1.0000'))
    print(y)
    break