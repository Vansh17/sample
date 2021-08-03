# nums= [12,14,89,67,78]
#
# for num in nums:
#     if num%5==0:
#         print(num)
#         break
# else:
#         print("not found")
#
#
# num = 7
# for i in range(2,num):
#     if num%i ==0:
#         print("not prime")
#         break
# else:
#     print("prime")


# from array import*
# vals = array('i',[5,78,-54,23,14])
# for i in range(5):
#     print(vals[i])

#
# from array import*
# vals = array('i',[5,78,-54,23,14])#i is the data type             buffer info is for the address, size
# newArr = array(vals.typecode,(a*a for a in vals))
# print(newArr)
#
#
#
# for e in newArr:
#
#     print(e)
#
#
# i = 0
# while i < len(newArr):
#     print(newArr[i])
#     i+=1
#
# #
# from array import *
# arr = array('i',[])
#
# n = int(input("enter the length of array"))
#
# for i in range(n):
#     x = int(input("enter the next value "))
#     arr.append(x)
#
#
# print(arr)
#
#
# vals = int(input("enter the value of search"))
# k=0
# for e in arr:
#     if e==vals:
#         print(k)
#         break
#     k+=1
#
# print(arr.index(vals ))

from numpy import *
arr = array([1,2,3,5,3,9],int)          # the 'int' is optional

print(arr)



