from array import *

arr = array('i', [])
n = int(input("enter the length: "))
for e in range(n):
    x = int(input("enter the values u want: "))
    arr.append(x)
print(arr)

val = int(input("enter the value for search: "))
k = 0
for i in arr:
    if (i == val):
        print(k)
        break
    k += 1
print(arr.index(val))
