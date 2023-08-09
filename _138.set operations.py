import  numpy as np
a=np.array([2,4,67,111,1,111,2,0,0,9,9,9])
print('unique element in array:',np.unique(a))

print('\nUNION OPERATION')
arr1=np.array([11,2,33,4,5,6])
arr2=np.array([6,7,89,56,00,67])
print('union of two array:',np.union1d(arr1,arr2))

print('\nINTERSECTION OPRATION')
print('intersection of array:',np.intersect1d(arr1,arr2))

print('\nDIFFERENCE OPERATION')
print('difference between arrays:',np.setdiff1d(arr1,arr2))