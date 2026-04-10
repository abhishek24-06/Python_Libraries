import numpy as np

rng= np.random.default_rng()

print(rng.integers(1,7)) #random numbers from 1-6
                        #like rolling dice
                        
print(rng.integers(1,101,(2,2))) #(low,high,(row,col))

#floating number
print(np.random.uniform(-1,1,(2,3)))

#shuffle array
rng=np.random.default_rng()
array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits=np.array(['Mango','Apple','Pineapple','Orange'])
fruits=rng.choice(fruits,(2,2))
print(fruits)
