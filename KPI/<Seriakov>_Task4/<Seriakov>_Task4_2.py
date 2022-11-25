from math import *
#'Introduction to programming':Task 4
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 4")
print("Seriakov Vlad, FB-21")
while(True):
    try:
        a = abs(int(input('Введіть ціле число:')))
        n = 1
        while(a >= 10):
            a = a / 10
            n += 1
        print ("Ви ввели " + str(n) + " цифр")  
        break
    except:
        print('Ви ввели не ціле число, або взагалі не число. Повторіть спробу')   