import numpy as np

array= np.array([[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12],
                [13,14,15]])

# array[start:end:step]

# print(array[::-1])

print(array[:, 0]) #for column slicing

print(array[::-1, ::-1])