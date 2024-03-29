import numpy as np
arr = np.arange(0,11)

##length
len(arr)

##filtering
arr[arr > 6]

##2d array
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
arr_2d.shape ##first row then column

arr_2d[2][2]
##You can also write more commonly
arr_2d[2,2]

##broadcasting
arr[0:2] = 99
#to avoid broadcasting use copy
arr_copy = arr.copy()

##operations
arr +5
arr/arr #divided by 0 will give you nah
arr.sum()
arr.mean()
arr.var()
arr.std()
arr_2d.sum(axis = 0)
arr_2d.sum(axis = 1)
