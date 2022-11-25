from array import *
#'Introduction to programming':Task 4
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 4")
print("Seriakov Vlad, FB-21")
sqrt = 1
xn = 1
e = 1e-4
a = float(input("Введіть число щоб отримати його корінь:"))
def x(xn, a):
    return (1/2)*(xn+a/xn)
if (a < 0):
    print('Неможливо це зробити')
elif(a == 0):
	print(0)
else:
    while abs(x(xn, a)-xn) > e:
        sqrt = x(xn, a)
        xn = sqrt
    if(round(sqrt, 4) - 0.0001 == round(sqrt, 1)):
        sqrt = round(sqrt, 1)
        print(round(sqrt, 1))
    else:
        print(round(sqrt, 4))