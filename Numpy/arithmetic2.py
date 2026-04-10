import numpy as np

#Element wise Arithmetic
array1=np.array([1,2,3])
array2=np.array([4,5,6])

# print(array1 + array2)
# print(array1 - array2)
# print(array1 * array2)
# print(array1 / array2)
# print(array1 ** array2)

#Comparison Arithmetic

scores=np.array([91,55,100,73,82,64])

print(scores==100)
print(scores>=60)

scores[scores <60] =0
print(scores)