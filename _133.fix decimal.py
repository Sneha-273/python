import numpy as np
arr1=np.array([-1,-11,-2,-3])
print("absolute:",abs(arr1))
arr2=np.array([-1.22203333,2.124356])
print("rounding decimal.........")
print('Method 1->truncate array:',np.trunc(arr2))
print('Method 2->fix decimal in array:',np.fix(arr2))
print('Method 3->increament preceding a digit:',np.around(arr2))
print('Method 4->nearest lower integer:',np.floor(arr2))
print('Method 5->nearest upper integer:',np.ceil(arr2))