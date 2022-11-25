#'Introduction to programming':Task 7.2
#Seriakov Vlad, FB-21
print("'Introduction to programming':Task 7.2")
print("Seriakov Vlad, FB-21")
n = int(input('Введіть число для перевірки:'))
def powerOF2chek(n):
    if(n == 1):
        return 'yes'
    elif(n > 1):
        return powerOF2chek(n/2)
    else:
       return 'no'
print(powerOF2chek(n))