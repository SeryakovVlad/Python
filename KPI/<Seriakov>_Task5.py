#'Introduction to programming':Task 5
#Seriakov Vlad, FB-21, V-2
print("'Introduction to programming':Task 5")
print("Seriakov Vlad, FB-21, V-2")
try:
    n = int((input('Введіть значення N:')))
    m = int((input('Введіть значення M:')))
    i = 0
    for i in range(n, m+1):
        if (int(i) % 2 == 0) or (int(i) % 3 == 0):
            print(i,)
        else:
            continue
except:
    print("Щось не так, спробуйте спробу")