#Get Started
import sys

#Intro
print("Hello, World!")
print(2+2)
print(10*2)

#Get Started
print(sys.version)

#Python Syntax
if 5 > 2:
    print("Five is greater than two!")

x = 5 # Integer variable
y = "Hello, World!" # String variable

print("Python is fun!")

print("Hello World!")
print("Have a good day.")
print("Learning Python is fun!")

print("Hello"); print("How are you?"); print("Bye bye!")

#Python Output
print("Hello World!")
print("I am learning Python.")
print("It is awesome!")

print("This will work!")
print('This will also work!')

print("Hello World!", end=" ") #new
print("I will print on the same line.")

print(3)
print(358)
print(50000)

print(3 + 3)
print(2 * 5)

print("I am", 1000, "years old")

#Python Comments
#This is a comment
print("Hello, World!") #This is a comment

#print("Hello, World!")
print("Cheers, Mate!")

#This is a comment
#written in 
#more than just one line
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#print("This should not run")

"""
This is
a multiline
comment
"""

#Python Variables
x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)

x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
print(type(x))
print(type(y))
print(type(z))

x = "John"
x = 'John'

x = 3
print(type(x))

a = 4
A = "Sally" #new
print(a)
print(A)

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

x, y, z = "Orange", "Banana", "Cherry" #new
print(x)
print(y)
print(z)

x = y = z = "Orange" #new
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits #new
print(x)
print(y)
print(z)

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x,y,z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

x = "awesome"

def myfunc2():
    x = "fantastic" #new
    print("Python is " + x)

myfunc2()

print("Python is " + x)

def myfunc3():
    global myfunc3variable #new
    myfunc3variable = "fantastic"

myfunc3()

print("Python is " + myfunc3variable)

myfunc4variable = "awesome"

def myfunc4():
    global myfunc4variable
    myfunc4variable = "fantastic"

myfunc4()

print("Python is " + myfunc4variable)

x = 5
y = "John"
print(type(x))