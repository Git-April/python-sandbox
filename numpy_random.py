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
# sns.displot([0, 1, 2, 3, 4, 5])
# plt.show()

# sns.displot([0, 1, 2, 3, 4, 5], kind="kde")
# plt.show()

#Normal Distribution
x = random.normal(size=(2, 3))
print(x)

x = random.normal(loc = 1, scale = 2, size=(2, 3))
print(x)

# sns.displot(random.normal(size=1000), kind="kde")
# plt.show()

#Binomial Distribution
x = random.binomial(n=10, p=0.5, size=10)
print(x)

# sns.displot(random.binomial(n=10, p=0.5, size=1000))
# plt.show()

data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}

# sns.displot(data, kind="kde")
# plt.show()

#Poisson Distribution
x = random.poisson(lam=2, size=10)
print(x)

# sns.displot(random.poisson(lam=2, size=1000))
# plt.show()

data = {
  "normal": random.normal(loc=50, scale=7, size=1000),
  "poisson": random.poisson(lam=50, size=1000)
}

# sns.displot(data, kind="kde")
# plt.show()

data = {
  "binomial": random.binomial(n=1000, p=0.01, size=1000),
  "poisson": random.poisson(lam=10, size=1000)
}
# sns.displot(data, kind="kde")
# plt.show()

#Uniform Distribution
x = random.uniform(size=(2, 3))
print(x)

sns.displot(random.uniform(size=1000), kind="kde")
plt.show()