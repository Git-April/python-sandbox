from numpy import random #Random Intro

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