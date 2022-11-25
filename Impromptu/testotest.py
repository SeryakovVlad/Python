arr = [23523,42524,'efwvs','5344fd','tfd43544','retsf4354e5']
newIntArr = []
newStrArr = []
m = 0
intValue = ''
strValue = ''
for i in range(len(arr)):
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