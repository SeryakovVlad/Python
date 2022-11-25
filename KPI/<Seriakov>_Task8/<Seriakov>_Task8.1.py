#'Introduction to programming':Task 8
#Seriakov Vlad, FB-21, V-7
print("Introduction to programming':Task 6")
print("Seriakov Vlad, FB-21, V-6")
arr1 = []
arr2 = []
while True:
    print('Якщо хочете закінчити вводити масив 1 то напишіть в значення масиву - no')
    a = input('введіть значення масиву:')
    if (a == 'no'):
        break
    else:
        a = int(a)
        arr1.append(a)
while True:
    print('Якщо хочете закінчити вводити масив 2 то напишіть в значення масиву - no')
    a = input('введіть значення масиву:')
    if (a == 'no'):
        break
    else:
        a = int(a)
        arr2.append(a)
print("Масив 1:" + str(arr1))
print("Масив 2:" + str(arr2))
newArr = arr1 + arr2
end = len(newArr) - 1
while end != 0:
    i = 0
    for i in range(end):
        if newArr[i] > newArr[i + 1]:
            newArr[i], newArr[i + 1] = newArr[i + 1], newArr[i]
    end = end - 1
print(newArr)