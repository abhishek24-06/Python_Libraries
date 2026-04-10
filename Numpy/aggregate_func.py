import numpy as np

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])  

# print(np.sum(array))
# print(np.mean(array)) 
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array)) #smallest index
# print(np.argmax(array)) #largest index

print(np.sum(array,axis=0)) #0 for column
print(np.sum(array,axis=1)) #1 for row