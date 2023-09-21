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
#random.radrange(start num,stop num)
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
#And we can use this in if statement
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#To check if a certain phrase or character is NOT present in a string:
txt = "The best things in life are free!"
print("expensive" not in txt)
#And we can use this in if statement
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#Specify the start index and the end index:
b = "Hello, World!"
#var name[start index : stop index]:
print(b[2:5])
#from start:
print(b[:5])
#to the end:
print(b[2:]) 
#we can use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

#for convert the sting in upper case:
a = "Hello, World!"
print(a.upper())
#for convert the sting in lower case:
a = "Hello, World!"
print(a.lower())

#for remove the Whitespace:
a = "    hello, world!"
print(a.strip())

#for replace a string with another one:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method returns a list where the text between the specified separator becomes the list items.
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#To concatenate, or combine, two strings you can use the + operator:
a = "Hello"
b = "World"
c = a + b
print(c)
#To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#we can combine strings and numbers by using the format() method!
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#To insert characters that are illegal in a string, use an escape character \"...\":
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
#              Code	             Result	             example                                             rtu
#              \'	             Single Quote	     txt = 'It\'s alright.'                           It's alright.
#              \\	             Backslash	         txt = "This will insert one \\ (backslash)."     This will insert one \ (backslash).
#              \n	             New Line	         
#              \r	             Carriage Return	
#              \t	             Tab	            txt = "Hello\tWorld!"                             Hello   World!
#              \b	             Backspace	
#              \f	             Form Feed	
#              \ooo	             Octal value	   txt = "\110\145\154\154\157"                       Hello
#              \xhh	             Hex value         txt = "\x48\x65\x6c\x6c\x6f"                       Hello

#The all method of string  
#    function                  Description                                                                                   example                              code                  return
#   capitalize()          	Converts the first character to upper case                                                       x = "hello,world!"                  x.capitalize()         Hello,world!
#   casefold()	            Converts string into lower case                                                                  x = "HELLO"                         x.casefold()           hello            
#   center()	            Returns a centered string                                                                        x = "HELLO"                         x.center(2)            ..HELLO # . == space 
#   count()	                Returns the number of times a specified value occurs in a string                                 x = "I love apples, apple are..."   x.count("apple")       2
#   encode()	            Returns an encoded version of the string                                                         x = "My name is Ståle"              x.encode()             b'My name is St\xc3\xe5le'
#   endswith()	            Returns true if the string ends with the specified value                                         x = "hello !"                       x.endswith()           True 
#   expandtabs()	        Sets the tab size of the string                                                                  x =  "hell\to"                      x.expandtabs(5)        hell     o
#   find()	                Searches the string for a specified value and returns the position of where it was found         x = "Hello, welcome to my"          x.find(to)             2
#   format_map()	        Formats specified values in a string     
#   index()	                Searches the string for a specified value and returns the position of where it was found         x = "Hello, welcome to my"          x.index("welcome")     7
#   isalnum()	            Returns True if all characters in the string are alphanumeric                                    x = "Company12"                     x.isalnum()            True 
#   isalpha()	            Returns True if all characters in the string are in the alphabet                                 x = "CompanyX"                      x.isalpha()            True
#   isascii()	            Returns True if all characters in the string are ascii characters                                x = "Company123"                    x.isascii()            True
#   isdecimal()             Returns True if all characters in the string are decimals                                        x = "1234"                          x.isdecimal()          True
#   isdigit()	            Returns True if all characters in the string are digits                                          x = "50800"                         x.isdigit()	        True                                  
#   isidentifier()	        Returns True if the string is an identifier                                                      x = "str"                           x.isidentifier()       True
#   islower()	            Returns True if all characters in the string are lower case                                      x = "str"                           x.islower()            True
#   isnumeric()	            Returns True if all characters in the string are numeric                                         x = "1234"                          x.isnumric()           True
#   isprintable()	        Returns True if all characters in the string are printable                                       x = "Hello! Are you #1?"            x.isprintable()	    True
#   isspace()               Returns True if all characters in the string are whitespaces                                     x = "  "                            x.isspace()            True
#   istitle()               Returns True if the string follows the rules of a title                                          x = "Hello, And Welcome To My"      x.istitle()            True
#   isupper()	            Returns True if all characters in the string are upper case                                      x = "HELLO"                         x.isupper()            True
#   join()	                Joins the elements of an iterable to the end of the string                                       x = ("John", "Peter", "Vicky")      s = "/".join(x)        John/Peter/Vicky 
#   ljust()	                Returns a left justified version of the string                                                   x = 
#   lower()	                Converts a string into lower case                                                                x = "HELLO"                         x.lower()              "hello"      
#   lstrip()	            Returns a left trim version of the string                                                        x = 
#   maketrans()             Returns a translation table to be used in translations                                           x = 
#   partition()             Returns a tuple where the string is parted into three parts                                      x = 
#   replace()	            Returns a string where a specified value is replaced with a specified value                      x = 
#   rfind()	                Searches the string for a specified value and returns the last position of where it was found    x = 
#   rindex()	            Searches the string for a specified value and returns the last position of where it was found    x = 
#   rjust()	                Returns a right justified version of the string                                                  x = 
#   rpartition()	        Returns a tuple where the string is parted into three parts                                      x = 
#   rsplit()	            Splits the string at the specified separator, and returns a list                                 x =   
#   rstrip()	            Returns a right trim version of the string                                                       x = 
#   split()	                Splits the string at the specified separator, and returns a list                                 x =
#   splitlines()	        Splits the string at line breaks and returns a list                                              x = 
#   startswith()	        Returns true if the string starts with the specified value                                       x =
#   strip()	                Returns a trimmed version of the string                                                          x =
#   swapcase()	            Swaps cases, lower case becomes upper case and vice versa                                        x = 
#   title()	                Converts the first character of each word to upper case                                          x = 
#   translate()             Returns a translated string                                                                      x =
#   upper()	                Converts a string into upper case                                                                x = "hello"                        x.upper()              "HELLO"
#   zfill()	                Fills the string with a specified number of 0 values at the beginning                            x =

#for check an objet is of a certain data type:
x = 200
print(isinstance(x, int))

#The logical operator
#Operator	     Name       	    Example	
#   +	        Addition	        x + y	
#   -	        Subtraction	        x - y	
#   *	        Multiplication	    x * y	
#   /	        Division	        x / y	
#   %	        Modulus	            x % y	
#   **	        Exponentiation	    x ** y	
#   //	        Floor division	    x // y

#The assignment operator
#Operator   Example     Same as
#   =	    x = 5	    x = 5	
#   +=	    x += 3	    x = x + 3	
#   -=	    x -= 3	    x = x - 3	
#   *=	    x *= 3	    x = x * 3	
#   /=	    x /= 3	    x = x / 3	
#   %=	    x %= 3	    x = x % 3	
#   //= 	x //= 3	    x = x // 3	
#   **= 	x **= 3	    x = x ** 3	
#   &=	    x &= 3	    x = x & 3	
#   |=	    x |= 3	    x = x | 3	
#   ^=	    x ^= 3	    x = x ^ 3	
#   >>= 	x >>= 3	    x = x >> 3	
#   <<= 	x <<= 3	    x = x << 3

#The  Comparison Operators
#Operator   Name	                   Example	
#   ==     Equal	                   x == y	
#   !=     Not equal	               x != y	
#   >	   Greater than                x > y	
#   <	   Less than	               x < y	
#   >=     Greater than or equal to    x >= y	
#   <=     Less than or equal to	   x <= y

#Logical Operators
#Operator	Description	                                                    Example	
#and 	    Returns True if both statements are true	                  x < 5 and  x < 10	
#or	        Returns True if one of the statements is true	              x < 5 or x < 4	
#not	    Reverse the result, returns False if the result is true	not   (x < 5 and x < 10)

#The Identity Operators
#Operator	Description	                                            Example	
#is     	Returns True if both variables are the same object	    x is y	
#is not	    Returns True if both variables are not the same object	x is not y

#The Membership Operators
#Operator	Description                                                                 	   Example
#in 	    Returns True if a sequence with the specified value is present in the object	   x in y	
#not in	    Returns True if a sequence with the specified value is not present in the object   x not in y

# The 
#Operator	    Name      Description	                                                                                                           Example	
#  &         	AND	      Sets each bit to 1 if both bits are 1                                                                                   	x & y	
#  |	        OR	      Sets each bit to 1 if one of two bits is 1	                                                                            x | y	
#  ^	        XOR	      Sets each bit to 1 if only one of two bits is 1	                                                                        x ^ y	
#  ~	        NOT	      Inverts all the bits	                                                                                                    ~x	
#  <<        	Zero      fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off                    	x << 2	
#  >>        	Signed    right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off     x >> 2

#The Array in python:
# type  |  brackets  |  ordered  |  mutable  |  duplicate  |     use      |
#-------|------------|----------------------------------------------------|
# list  |     []     |    yes    |    yes    |     yes     |      عام     |
# tuple |     ()     |    yes    |    no     |     yes     |    احداثيات    |
# set   |     {}     |    no     |    no     |     no      | العمليات الرياضة |
# dict  |     {}     |    key    |    yes    |   yes/no    |  قواعد البيانات  |

# --------------------list--------------------------#
# brackets
num = [1,4.5,"hello",[1.5,2],True]
print(num)
# ordered
print(num[2])
# mutable
num[1] = 'ali'
print(num)
# duplicate
num = [1,1,1,1]
print(num)
#chengeable: we can add and remove items in a list after it has been created

#---------------------tuple--------------------------#
# brackets
my_tuple = (1,4.5,"hello",[1.5,2],True)
print(my_tuple)
# ordered
print(my_tuple[2])
#duplicate
my_tuple = (1,1,1,1)
print(my_tuple)
#----------------------set---------------------------#
#brackets
my_set = ("ahmed","ali","laib","raouf")
print(my_set)
#---------------------dict---------------------------#
# brackets
car = {
    "color":"red",
    "model":2022,
    "price":200000
}
# ordered
print(car["color"])
# mutable
car["color"] = "black"
print(car["color"])
# duplicate
car = {
    "color":"red",
    "model":2022,
    "color":"black",#no
    "colore":"red"#yes
}
print(car)

#for give The number elements of list we use len:
li = ["abderaouf","laib",15,2.03,-1,True]
print(len(li)) 
#The type of list is list:
print(type(li))
#for constracte a list It have 2 methode:
#1st methode: Simple methode;
#2nd methode: we use list() function
lis = list(("raouf",True,15,2.01,'Hayt '))

#Negative Indexing
#Negative indexing means start from the end: -1 refers to the last item, -2 refers to the second last item etc.

#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#For chenge a list we have existe 2methods
#1st Method change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#range
#two values with two values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#two values with one value
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

#one value with two values
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#2nd method
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.
#The insert() method inserts an item at the specified index:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#To append elements from another list to the current list, use the extend() method:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#The remove() or del() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
del thislist[2]
print(thislist)
#we can delete the list 
del thislist

#for remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#removeing only the content of list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#You can loop through the list items by using a for loop:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#You can also loop through the list items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#You can loop through the list items by using a while loop.
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#Looping Using List Comprehension
#List Comprehension offers the shortest syntax for looping through lists:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#to write a short syntex for creating the new list from an old list:
#The syntax:
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)




















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

#this same values are return False: False , None , 0 , "" ,() , [] ,{}

#The precedence order is described in the table below, starting with the highest precedence at the top:
#Operator	                                        Description	
# ()	                                            Parentheses	
# **	                                            Exponentiation	
# +x -x  ~x                                        	Unary plus, unary minus, and bitwise NOT	
# * /  //  %	                                    Multiplication, division, floor division, and modulus	
# + -	                                            Addition and subtraction	
# << >>	                                            Bitwise left and right shifts	
# &	                                                Bitwise AND	
# ^	                                                Bitwise XOR	
# |	                                                Bitwise OR	
# == !=  >  >=  <  <=  is  is not  in  not in 	    Comparisons, identity, and membership operators	
# not                                               Logical NOT	
# and                                               AND	
# or	                                            OR
#-Note: There are some list methods that will change the order, but in general: the order of the items will not change.
#-Note: The length of the list will change when the number of items inserted does not match the number of items replaced.
