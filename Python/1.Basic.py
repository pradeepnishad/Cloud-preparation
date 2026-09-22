
# how to print hello world in python

print("helo world")

# how to print python version

from ctypes.wintypes import BOOLEAN
import sys
print(sys.version)


print("hello world", end=" ")  # this will print hello world without a new line at the end
print("hello mouse")


# this is used to put a comment in python code
"""this is a multi line comment in python"""

X = 5 # this is a variable assignment in python
print(type(X)) # this will print the type of variable X

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.


a,b,c = 5,10,"hello" # this is a multiple variable assignment in python
print(a,b,c) # this will print the values of variables a, b and c

x = y = z = 10 # this is a multiple variable assignment in python
print(x,y,z) # this will print the values of variables x, y and z


# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


# Built-in Data Types
# In programming, data type is an important concept.

# Variables can store data of different types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# there are three numeric types in Python:

# int
# float
# complexT

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

int1 = 1 
print(int1) # this will print the value of variable int1
print(type(int1)) # this will print the type of variable int1


# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -35.59

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# Complex
# Complex numbers are written with a "j" as the imaginary part:

x = 3+5j
y = 5j
z = -5j

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random
random_number = random.randrange(1, 10) # this will generate a random number between 1 and 10
print(random_number) # this will print the random number generated

# Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
# str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals


# Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# Floats:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


# Strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")
print('Hello')


# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)


# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

a = "Hello, World!"
print(a[1])


# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.

for x in "banana":
  print(x, end=" ")
   # this will print each character in the string "banana" on the same line with a space in between

print() # this will print a new line

# String Length
# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a))

# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

txt = "The best things in life are free!"
print("free" in txt)


# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.

txt = "The best things in life are free!"
print("expensive" not in txt)


# Boolean Values
# Boolean values are either True or False.
print(10 > 9)
print(10 == 9)
print(10 < 9)   


# Python Operators
# Operators are used to perform operations on variables and values.

# In the example below, we use the + operator to add together two values:

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)


# Python Arithmetic Operators

# Operator	Name	Example	Try it
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	

x = 15
y = 4

print(x + y)    
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y) # Floor division always returns an integer. It rounds DOWN to the nearest integer:



# Python Assignment Operators

# Operator	Example	Same As	Try it
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3)	x = 3 print(x)


# The Ternary Operator
# The ternary operator allows you to assign one value if a condition is true, and another if it is false:

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

# Comparison Operators
# Comparison operators are used to compare two values:

# Operator	Name	Example	Try it
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

x = 5

print(x > 0 and x < 10)

# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator	Description	Example	Try it
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y


# The is operator returns True if both variables point to the same object:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	Description	Example	Try it
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)


# Bitwise operators are used to compare (binary) numbers:

# Operator	Name	Description	Example	Try it
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2

# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

print(6 & 3)
# The binary representation of 6 is 0110
# The binary representation of 3 is 0011

# Then the & operator compares the bits and returns 0010, which is 2 in decimal.


# Operator Precedence
# Operator precedence describes the order in which operations are performed.

# Precedence Order
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator	Description	Try it
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR


