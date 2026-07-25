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

x = 5
y = 3.15
z = 2+3j
print(type(x))
print(type(y))
print(type(z))

#Python Casting
x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)

x = float(1)
y = float(2.8)
z = float("3")
w = float("4.2")
print(x)
print(y)
print(z)
print(w)

x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

x = 1
a = float(x)
b = str(x)
print(a)
print(b)

#Python Strings
print("Hello")
print('Hello')

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))
print(a.split("o"))

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

txt = "\' \\ \n \r \t a\b \f \x53"
print(txt)

txt = "Hello, World!"
print(txt[2:5])
print(txt.upper())
name = "Python"
print(f"I love {name}")

#Python Booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

print(bool("Hello"))
print(bool(15))

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

def myFunction():
    return True

print(myFunction())

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 200
print(isinstance(x, int))

print(10 > 9)
print(10 == 9)
print(bool("Hello"))
print(bool(0))

#Python Operators
print(10 + 5)

sum1 = 100 + 50
sum2 = sum1 + 250
sum3 = sum2 + sum2

x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

x = 12
y = 5
print(x / y)
print(x // y)

print(x & 3)
print(x | 3)
print(x >> 3)
print(x << 3)
print(x:=3)
print(x)

numbers = [1, 2, 3, 4, 5]
if(count := len(numbers)) > 3: #new
    print(f"List has {count} elements")

num = 6
x = "WEEKEND!" if num > 5 else "Workday"
print(x)

num = 6
x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday" #new
print(x)

x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)

x = 5
print(x > 0 and x < 10)
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #new
print(x is y)
print(x == y)
print(x is not y)

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)

print((6 + 3) - (6 - 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)

a = 15
b = 4
print(a % b)
print(a // b)
print(a ** b)
a += 10