#First code in python:
print("hello world!")

#Indentation is very important in PY because it is used to denote a block of code.
if 2 < 5:
    print("2 < 5")

#ERROR:
#if 2 < 5:
#print("2 < 5")
 
#The comments: use # to comment a one line and use """ to comment multi line 

#The varibles
x = 2
X = 4
y = "hello world "
z = 'hay, can you help me'
#To specify the data type of the variable
x = int(3) # x will be 3
y = str(3) # x will be '3'
d = float(3) #x will be 3.0
Name, familyName = "raouf","laib"
a = b = 2
Fruit = ["apple","banana"]
x,y = Fruit

#To get the data type of the variable
x = 3
type(x)

#The output of varible
print(x)
print(x,y)
print("int ",a + b)
print("string ",y + z)

#GLobal varible and local varible:
m = "hello" #Global varible
print(m)
def var_fonction():
    mn = 4 #Locale varible 
    print(mn, m)
    

var_fonction()

#To create a global variable inside a function:
def My_fon():
    global s 
    s = 5
My_fon()
print(s)

#Data Type:

#Text Type:	    str
#Numeric Types:	int, float, complex
#Sequence Types:list, tuple, range
#Mapping Type:  dict
#Set Types:	    set, frozenset
#Boolean Type:	bool
#Binary Types:	bytes, bytearray, memoryview
#None Type:	    NoneType

#Example:
x = "Hello World"	                          #str	
x = 20	                                      #int	
x = 20.5	                                  #float	
x = 1j	                                      #complex	
x = ["apple", "banana", "cherry"]	          #list	
x = ("apple", "banana", "cherry")	          #tuple	
x = range(6)	                              #range	
x = {"name" : "John", "age" : 36}	          #dict	
x = {"apple", "banana", "cherry"}	          #set	
x = frozenset({"apple", "banana", "cherry"})  #frozenset	
x = True                	                  #bool	
x = b"Hello"	                              #bytes	
x = bytearray(5)	                          #bytearray	
x = memoryview(bytes(5))	                  #memoryview	
x = None
#random function
import random
#random.radrange(first num,secound num)
print("ran",random.randrange(1, 100))
#You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
  #or
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#for get only one varible in python
print("var",a[5])
# we can loop through the characters in a string:
for x in "banana":
  print(x)
#To get the length of a string, use the len() function:
a = "Hello, World!"
print(len(a))
#To check if a certain phrase or character is present in a string, we can use the keyword in:
txt = "The best things in life are free!"
print("free" in txt)#The result is True or False




#COMMENTS:
#-The number of spaces is up to use as a programmer but it has to be at least one; 
#And we have to use the same of spaces number in the block of code! 
if 5 < 2:
    print("5 < 2")
if 2 < 5:
        print("5 < 2")
#-python is accepte the power of 10 and he he was write:
power = 12e4
 #or 
powera = 12E4
#-You can convert from one type to another with the int(), float(), and complex() methods and You cannot convert complex numbers into another number type.:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

