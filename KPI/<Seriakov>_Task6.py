from itertools import groupby
#'Introduction to programming':Task 6
#Seriakov Vlad, FB-21, V-6
print("Introduction to programming':Task 6")
print("Seriakov Vlad, FB-21, V-6")
arr = []
while True:
    print('Якщо хочете закінчити вводити масив то напишіть в значення масиву - no')
    a = input('введіть значення масиву:')
    if (a == 'no'):
        break
    else:
        a = int(a)
        arr.append(a)
arr.sort()
arr.reverse()
arr = [el for el, _ in groupby(arr)]
print(arr)
value = int(input('Ввдеіть число яке ви хочете знайти:'))
def binarySearch(arr, index):
    start = len(arr) - 1
    end = 0
    while (start >= end):
        mid = (start + end)//2
        if(arr[mid] == index):
            return mid
        elif(arr[mid] > index):
            end = mid + 1
        else:
            start = mid - 1
    return -1
res = (value, binarySearch(arr, value))
print(res)