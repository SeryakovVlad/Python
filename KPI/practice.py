from copy import deepcopy
a = [[1,2],3]
print(a)
b = deepcopy(a)
print(a is b)
print(a[0] is b[0])
b[0][0] = 0
print(b)
print(a)
#indirection
#big O notation