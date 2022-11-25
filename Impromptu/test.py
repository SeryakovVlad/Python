from itertools import groupby
print('Input figure to the array, if you want to stop inputting figure - input "NaN"')
arr = []
a = 1

while True: #inputting figures to the arrays
    i = input('Input ' + str(a) + 'ʼs figure:')
    if(i == ''):
        break
    else:
        a = int(a)
        a += 1
        try:
            arr.append(int(i))
        except:
            arr.append(i)

i = 0
newIntArr = []
newStrArr = []
m = 0
intValue = ''
strValue = ''
for i in range(len(arr)): #converting 'a1b2c3d4' to 'abcd', '1234'
    if(type(arr[i] == str)):
        strElementArr = list(arr[i])
        for n in range(len(strElementArr)):
            try:
                strElementArr[n] = int(strElementArr[n])
                newIntArr.append(strElementArr[n])
                for m in range(len(newIntArr)):
                    intValue += str(newIntArr[m])
                arr.append(int(intValue))
            except:
                for m in range(len(newIntArr)):
                    strValue += str(newIntArr[m])
                arr.append(strValue)
    else:
        continue

print(arr)
end = len(arr) - 1
i = 0
lastElement = arr[len(arr) - 1]
def sortingLeftToRight(arr,i):
    while(i <= end): #int figure to left and str figure to right
        try:
            (arr[i] == int(arr[i]))
            i += 1
        except:
            arr.append(arr[i])
            arr.remove(arr[i])
        if(lastElement == arr[i]):
            break
sortingLeftToRight(arr,i)
for j in range(len(arr)): #finding last int figure to sort int figure in array
    try:
        j = int(arr[j])
    except:
        break
intArr = arr[0:j]
intArr.sort()
intArr.reverse()
k = 0
while(k <= j): #sorting int arr
    if(type(arr[k]) == int):
        arr.remove(arr[k])
    else:
        break
j = 0
for j in range(len(intArr)):
    arr = [intArr[j]] + arr
i = 0
sortingLeftToRight(arr,i)
print(arr)