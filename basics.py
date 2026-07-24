import sys #Get Started
import random #Python Numbers

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

#Python Data Types
x = 5
print(type(x))

x = 1j #new
print(type(x))

x = "Hello World" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["apple", "banana", "cherry"] #list
x = ("apple", "banana", "cherry") #tuple #new
x = {"apple", "banana", "cherry"} #set #new
print(x)
x = range(6) #range
print(x)
x = {"name": "John", "age": 36} #dict
x = frozenset({"apple", "banana", "cherry"}) #frozenset
print(x)
x = 5
print(x)
x = True #bool
print(x)
x = b"Hello" #bytes
print(x)
x = bytearray(5) #bytearray
print(x)
x = memoryview(bytes(5)) #memoryview
print(x)
x = None #NoneType
print(x)
print(type(x))

x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = set(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)
x = frozenset(("apple", "banana", "cherry"))
x = bool(5)
print(x)
x = bytes(5)
x = bytearray(5)
x = memoryview(bytes(5))

x = 5
y = 3.14
z = "Hello"
print(type(x))
print(type(y))
print(type(z))

#Python Numbers
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

x = 3+5j
y = 5j
z = -5j
print(type(x))
print(type(y))
print(type(z))

x = 1
y = 2.8
z = 1j
a = float(x)
b = int(y)
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

print(random.randrange(1, 10))