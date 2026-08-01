from numpy import random #Random Intro
import numpy as np #Random Permutation
import matplotlib.pyplot as plt #Seaborn Module
import seaborn as sns #Seaborn Module

#Random Intro
x = random.randint(100)
print(x)

x = random.rand()
print(x)

x = random.randint(100, size=(5))
print(x)

x = random.randint(100, size=(3, 5))
print(x)

x = random.rand(5)
print(x)

x = random.rand(3, 5)
print(x)

x = random.choice([3, 5, 7, 9])
print(x)

x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

#Data Distribution
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6 ,0.0], size=(100))
print(x)

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

#Random Permutation
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)

arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

#Seaborn Module
#sns.displot([0, 1, 2, 3, 4, 5])

sns.displot([0, 1, 2, 3, 4, 5], kind="kde")

plt.show()