#'Introduction to programming':Task 8
#Seriakov Vlad, FB-21, V-7
print("Introduction to programming':Task 6")
print("Seriakov Vlad, FB-21, V-6")
arr1 = []
arr2 = []
while True:
    print('Якщо хочете закінчити вводити масив 1 то напишіть в значення масиву - no')
    i = input('введіть значення масиву:')
    if (i == 'no'):
        break
    else:
        i = int(i)
        arr1.append(i)
while True:
    print('Якщо хочете закінчити вводити масив 2 то напишіть в значення масиву - no')
    i = input('введіть значення масиву:')
    if (i == 'no'):
        break
    else:
        i = int(i)
        arr2.append(i)
print("Масив 1:" + str(arr1))
print("Масив 2:" + str(arr2))
newArr = arr1 + arr2
def insert(newArr, i):
    value = newArr[i]
    j=i
    while j != 0 and newArr[j - 1] > value:
        newArr[j] = newArr[j-1]
        j -= 1
    newArr[j] = value
def insertion_sort(newArr):
    for i in range(len(newArr)):
        insert(newArr, i)
insertion_sort(newArr)
print(newArr)