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
def get_index_of_smallest(newArr, i):
    index_of_smallest = i
    for j in range(i + 1, len(newArr)):
        if newArr[j] < newArr[index_of_smallest]:
            index_of_smallest = j
    return index_of_smallest
def selection_sort(newArr):
    for i in range(len(newArr)):
        index_of_smallest = get_index_of_smallest(newArr, i)
        newArr[i], newArr[index_of_smallest] = newArr[index_of_smallest], newArr[i]
selection_sort(newArr)
print(newArr)