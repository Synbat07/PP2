# HOME
print("Hello World!")

# Syntax
if 5 > 2:
  print("Five is greater than two!")

# Variables
x = 7
y = "Synbat"
print(x)
print(y)


# Names
myvar = "John"
print(myvar)

# Multiple Values
#1)
x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)

#2)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
#1)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#2)
x = 5
y = 10
print(x + y)

#Global Variables
#1)
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#2)
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Data Types
# 1)
x = 5
print(type(x))

#2)
x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))

# Casting
#1)
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#2)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


#STRINGS
print("Hello")

#Slicing Strings
# 1)
b = "Hello, World!"
print(b[2:5])  #llo

# 2)
b = "Hello, World!"
print(b[:5]) #Hello

#Modify Strings
#1)
a = "Hello, World!"
print(a.upper())
#2)
a = "Hello, World!"
print(a.lower())
#3)
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#F-Strings (String Format)
age = 36
txt = f"My name is John, I am {age}"
print(txt)   #My name is John, I am 36

#Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
