import sys #Get Started
import random #Python Numbers
import functools #Python Functions
import basics_modules as bm #Python Modules
import platform #Python Modules
import datetime #Python Dates
import math #Python Math
import json #Python JSON
import re #Python RegEx

#Python Intro
print("Hello, World!")
print(2+2)
print(10*2)

#Python Get Started
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

#Python Lists
mylist = ["apple", "banana", "cherry"]
thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry"))
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thisdictionary = {"kiwi": "orange"}
thislist.extend(thisdictionary)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist] #new

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist.append("test")
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist
print(mylist)

thislist.append("test")
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)

print(list1)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(mylist[1:4])

colors = ["red", "green", "blue"]
print(colors[0])
colors[1] = "yellow"
colors.append("purple")
colors.remove("red")
print(colors)

#Python Tuples
mytuple = ("apple", "banana", "cherry")
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = ("apple",) #new
print(type(thistuple))

thistuple = ("apple")
print(type(thistuple))

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

thistuple = ("apple", "banana", "cherry")
print(type(mytuple))

thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #new
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 #new
print(mytuple)

fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(len(fruits))
(a, b, c) = fruits
print(b)

#Python Sets
myset = {"apple", "banana", "cherry"}

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2} #new
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

set1 = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry"))
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
thisset.discard("banana") #new
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset

thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 #new
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "banana", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)
print(set1)

set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2 #new
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

colors = {"red", "green", "blue"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(len(colors))

#Python Dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)
print(type(x))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

x = thisdict.values()
print(x)
print(type(x))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)
car["year"] = 2020
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x)
car["color"] = "red"
print(x)

x = car.items()
print(x)
print(type(x))

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)
car["year"] = 2020
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x)
car["color"] = "red"
print(x)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

myfamily = {
    "child1" : {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily["child2"]["name"])

for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

car = {"brand": "Ford", "model": "Mustang", "year": 2024}
print(car["model"])
car["color"] = "red"
car.pop("brand")
print(car)

#Python If...Else
a = 33
b = 200
if b > a:
    print("b is greater than a")

number = 15
if number > 0:
    print("The number is positive")

age = 20
if age >= 18:
    print("You are an adult")
    print("You can vote")
    print("You have full legal rights")

is_logged_in = True
if is_logged_in:
    print("Welcome back!")

a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")

age = 25

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >= 65:
    print("You are a senior")

day = 3

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

number = 7

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

temperature = 22

if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside")
elif temperature > 10:
    print("It's cool outside")
else:
    print("It's cold outside")

username = "Emil"

if len(username) > 0:
    print(f"Welcome, {username}!")
else:
    print("Error: Username cannot be empty")

a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B") #new

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount applies!")

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Great day for outdoor activities!")

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
    print("Login successful")
else:
    print("Login failed")

score = 85

if score >= 0 and score <= 100:
    print("Valid score")
else:
    print("Invalid score")

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

age = 25
has_license = True
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You are too young to drive")

score = 85
attendance = 90
submitted = True

if score >= 60:
    if attendance >= 80:
        if submitted:
            print("Pass with good standing")
        else:
            print("Pass but with missing assignmment")
    else:
        print("Pass but low attendance")
else:
    print("Fail")

temperature = 25
is_sunny = True

if temperature > 20:
    if is_sunny:
        print("Perfect beach weather!")

temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
    print("Perfect beach weather!")

username = "Emil"
password = "python123"
is_active = True

if username:
    if password:
        if is_active:
            print("Login successful")
        else:
            print("Account is not active")
    else:
        print("Password required")
else:
    print("Username required")

score = 92
extra_credit = 5

if score >= 90:
    if extra_credit > 0:
        print("A+ grade")
    else:
        print("A grade")
elif score >= 80:
    print("B grade")
else:
    print("C grade or below")

a = 33
b = 200
if b > a:
    pass

age = 16
if age < 18:
    pass
else:
    print("Access granted")

score = 85

if score > 90:
    pass
print("Score processed")

value = 50

if value < 0:
    print("Negative value")
elif value == 0:
    pass
else:
    print("Positive value")

def caldulate_discount(price):
    pass

age = 20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

#Python Match
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _: #new
        print("Looking forward to the Weekend")

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4: #new
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

day = 3
match day:
    case 3:
        print("Wednesday")
    case _:
        print("Other day")

#Python While Loops
i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i ==3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else: #new
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

#Python Functions
def my_function():
    print("Hello from a function")

my_function()

my_function()
my_function()
my_function()

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius1)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

print(get_greeting())

def my_function():
    pass

my_function()

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name):
    print("Hello", name)

my_function("Emil")

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

def my_function(name = "friend"):
    print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Norway"):
    print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

def my_function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

def my_function(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

def my_function(x, y):
    return x + y

result = my_function(5, 3)
print(result)

def my_function():
    return["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function(name, /): #new
    print("Hello", name)
my_function("Emil")

def my_function(name):
    print("Hello", name)
my_function(name = "Emil")

def my_function(*, name): #new
    print("Hello", name)
my_function(name = "Emil")

def my_function(name):
    print("Hello", name)
my_function("Emil")

def my_function(a, b, /, *, c, d):
    return a + b + c + d
result = my_function(5, 10, c = 15, d = 20)
print(result)

def my_function(*kids): #new
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)
    
my_function("Emil", "Tobias", "Linus")

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

def my_function(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

def my_function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function(3, 7, 2, 9, 1))

def my_function(**myvar): #new
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)
my_function(name = "Tobias", age = 30, city = "Bergen")

def my_function(username, **details):
    print("Username:", username)
    print("Additional details:")
    for key, value in details.items():
        print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_function(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) #new
print(result)

def my_function(fname, lname):
    print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)

def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x = 300

def myfunc():
    print(x)

myfunc()

print(x)

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

def myfunc():
    global x
    x = 300

myfunc()

print(x)

x = 300

def myfunc():
    global x
    x = 200

myfunc()

print(x)

def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x #new
        x = "hello"
    myfunc2()
    return x
print(myfunc1())

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("Inner:", x)
    inner()
    print("Outer:", x)

outer()
print("Global:", x)

def changecase(func): #new
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Hello Sally"
print(myfunction())

def beforeafter(func):
    def inner():
        print("Before")
        func()
        print("After")
    return inner
@beforeafter
def test():
    print("During")
test()

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello Sally"

@changecase
def otherfunction():
    return "I am speed!"

print(myfunction())
print(otherfunction())

def changecase(func):
    def myinner(x):
        return func(x).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

print(myfunction("John"))

def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam

print(myfunction("John"))

def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase
@changecase(1) #new
def myfunction():
    return "Hello Linus"
print(myfunction())

def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + " Have a good day!"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Tobias"

print(myfunction())

def myfunction():
    return "Have a great day!"
print(myfunction.__name__) #new

def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Have a great day!"
print(myfunction.__name__)

def changecase(func):
    @functools.wraps(func) #new
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return "Have a great day!"
print(myfunction.__name__)

x = lambda a : a + 10 #new
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

a = ['1', '2']
ints = map(int, a)
print(ints)
print(list(ints))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

def secondlettera(fruit):
    return fruit[1] == "a"
fruits = ["and", "banana", "mango"]
filtered = filter(secondlettera, fruits)
print(filtered)
print(list(filtered))

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x : len(x))
print(sorted_words)

def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

def factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        print(n)
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]
print(sum_list(my_list))

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))

print(sys.getrecursionlimit())

sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

def my_generator(): #new
    yield 1
    yield 2
    yield 3
for value in my_generator():
    print(value)

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for num in count_up_to(5):
    print(num)

def large_sequence(n):
    for i in range(n):
        yield i
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

gen = large_sequence(2)
print(next(gen))
print(next(gen))

def simple_gen():
    yield "Emil"
    yield "Tobias"
    yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

list_comp = [x * x for x in range(5)]
print(list_comp)

gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

total = sum(x * x for x in range(10))
print(total)

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
gen = fibonacci()
for _ in range(100): #new
    print(next(gen))

def echo_generator():
    while True:
        received = yield
        print("Received:", received)
gen = echo_generator()
next(gen)
gen.send("Hello") #new
gen.send("World")

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close() #new

def greet(name):
    print("Hello", name)

greet("Emil")

#Python Range
x = range(10)
print(x)

x = range(3, 10)
print(x)

x = range(3, 10, 2)
print(x)

for i in range(10):
    print(i)

print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))

r = range(10)
print(r[2])
print(r[:3])

r = range(0, 10, 2)
print(6 in r)
print(7 in r)

r = range(0, 10, 2)
print(len(r))

for i in range(6):
    print(i)
for i in range(2, 6):
    print(i)

#Python Arrays
cars = ["Ford", "Volvo", "BMW"]

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
    print(x)

cars.append("Honda")

cars.pop(1)

cars.remove("BMW")

cars = ["Ford", "Volvo", "BMW"]
print(cars[0])
cars[1] = "Toyota"
print(cars)

#Python Iterators
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit)) #new
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

mystr = "banana"

for x in mystr:
    print(x)

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))

#Python Modules
bm.greeting("Jonathan")

a = bm.person1["age"]
print(a)

x = platform.system()
print(x)

x = dir(platform) #new
print(x)

print(dir(bm))

print(platform.system())

#Python Dates
x = datetime.datetime.now()
print(x)

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)
print(x)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

x = datetime.datetime.now()
print(x.strftime("%Y"))

#Python Math
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

x = abs(-7.25)

print(x)

x = pow(4, 3)

print(x)

x = math.sqrt(64)
print(x)

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

x = math.pi
print(x)

print(min(5, 10))
print(max(5, 10))
print(abs(-7.25))
print(pow(4, 3))

#Python JSON
x = '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

y = json.dumps(x)

print(y)

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorded": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

print(json.dumps(x))

json.dumps(x, indent=4)
print(json.dumps(x, indent=4))

json.dumps(x, indent=4, separators=(". ", " = "))
print(json.dumps(x, indent=4, separators=(". ", " = ")))

json.dumps(x, indent=4, sort_keys=True)
print(json.dumps(x, indent=4, sort_keys=True))

x = '{"name":"Emil", "age":30}'
y = json.loads(x)
print(y["age"])

#Python RegEx
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)

print(re.split(" ", txt))

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

txt = "The rain in Spain"
x = re.search("Spain", txt)
print(x.span())