#'Introduction to programming':Task 1
#Seriakov Vlad, FB-21, V-9(22)
import re
inputted = lambda inputter: re.findall(r'\w+', inputter)
arr_with_duplicates = inputted(input('Введіть слова через пробіл: '))
arr_without_duplicates = []
counter = 0
index_sort = range(0, len(arr_with_duplicates))
for i in range(0, len(arr_with_duplicates)):
    for j in index_sort[i+1:]:
        if arr_with_duplicates[i] == arr_with_duplicates[j]:
            counter += 1
        else:
            continue
    for j in index_sort[:i]:
        if arr_with_duplicates[i] == arr_with_duplicates[j]:
            counter += 1
        else:
            continue
    if counter == 0:
        arr_without_duplicates.append(arr_with_duplicates[i])
    counter = 0
print(arr_without_duplicates)