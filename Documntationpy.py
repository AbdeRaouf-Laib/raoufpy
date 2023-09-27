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

#:# = "Hello World"	                          #str	
x = 20	                                      #int	
x = 20.5	                                  #float	
x = 1j	                                      #complex	
x= ["apple", "banana", "cherry"]	          #list	
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
#Operator	     Name       	    	
#   +	        Addition	      #x + y	
#   -	        Subtraction	       x - y	
#   *	        Multiplication	    x * y	
#   /	        Division	        x / y	
#   %	        Modulus	           x % y	
#   **	        Exponentiation	    x ** y	
#   //	        Floor division	    x // y

#The assignment operator
#Operator        Same as
#   =	    #= 5	    x = 5	
#   +=	   x += 3	    x = x + 3	
#   -=	    x -= 3	    x = x - 3	
#   *=	    x *= 3	    x = x * 3	
#   /=	   x /= 3	    x = x / 3	
#   %=	    x %= 3	    x = x % 3	
#   //= 	x //= 3	    x = x // 3	
#   **= 	x **= 3	    x = x ** 3	
#   &=	    x &= 3	    x = x & 3	
#   |=	    x |= 3	    x = x | 3	
#   ^=	    x ^= 3	    x = x ^ 3	
#   >>= 	x >>= 3	    x = x >> 3	
#   <<= 	x <<= 3	    x = x << 3

#The  Comparison Operators
#Operator   Name	                   	
#   ==     Equal	                 #x == y	
#   !=     Not equal	              x != y	
#   >	   Greater than                x > y	
#   <	   Less than	               x < y	
#   >=     Greater than or equal t    x >= y	
#   <=     Less than or equal to	   x <= y

#Logical Operators
#Operator	Description	                                                    	
#and 	    Returns True if both statements are true	                  x #5 and  x < 10	
#or	        Returns True if one of the statements is true	               < 5 or x < 4	
#not	    Reverse the result, returns False if the result is true	not   (x < 5 and x < 10)

#The Identity Operator
#Operator	Description	                                            	
#is     	Returns True if both variables are the same object	  #x is y	
#is not	    Returns True if both variables are not the same objet	x is not y

#The Membership Operators
#Operator	Description                                                                	   
#in 	    Returns True if a sequence with the specified value is present in the object	 #x in y	
#not in	    Returns True if a sequence with the specified value is not present in the objct   x not in y

# The 
#Operator	    Name      Description	                                                                                                          	
#  &         	AND	      Sets each bit to 1 if both bits are 1                                                                                # 	x & y	
#  |	        OR	      Sets each bit to 1 if one of two bits is 1	                                                                           x | y	
#  ^	        XOR	      Sets each bit to 1 if only one of two bits is 1	                                                                        x ^ y	
#  ~	        NOT	      Inverts all the bits	                                                                                                    ~x	
#  <<        	Zero      fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off                   	x << 2	
#  >>        	Signed    right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off     x >> 2

#The Array in python:
# type  |  brackets  |  ordered  |  mutable  |  duplicate  |        use       |
#-------|------------|--------------------------------------------------------|
# list  |     []     |    yes    |    yes    |     yes     |        عام       |
# tuple |     ()     |    yes    |    no     |     yes     |     احداثيات     |
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
del thislist[1]
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
#for sorting the list:
#alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#Case Insensitive Sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy a List
#1st method
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#2nd method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join two list:
#1st method
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#2nd method
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)
#we can use the extend() method, where the purpose is to add elements from one list to another list:
#Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

#list method:
# Method	        Description
# append()       Adds an element at the end of the list
# clear()        Removes all the elements from the list
# copy()	       Returns a copy of the list
# count()        Returns the number of elements with the specified value
# extend()       Add the elements of a list (or any iterable), to the end of the current list
# index()        Returns the index of the first element with the specified value
# insert()       Adds an element at the specified position
# pop()	         Removes the element at the specified position
# remove()       Removes the item with the specified value
# reverse()      Reverses the order of the list
# sort()	       Sorts the list

#Create a Tuple:
#1st method
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#2nd method
thisTuple1 = tuple(("apple", "banana", "cherry"))
print(thisTuple1)

#in The Tuple for create only one item we should adding the , in the end of tuple
thistuple = ("apple",)
print(type(thistuple))
#To access the tuple we use the same list

#Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple2 = tuple(y)
print(thistuple2)
#Create a new tuple with the value "orange", and add that tuple:
thistuple3 = ("apple", "banana", "cherry")
y = ("orange",)
thistuple3 += y
print(thistuple3)

#To remove an item in the Tuple:
#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple

#in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Loop in tuple is same as list
#To join and multiply tuple we use '+' To join and we use '*' To multiply:
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

# Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

#A set is a collection which is unordered, unchangeable*, and unindexed.
#Sets are written with curly brackets.
#Create a Set:
#1st Method:
thisset = {"apple", "banana", "cherry"}
print(thisset)
#2nd Method:
Thisset = set(("lain","la","aa",2))
print(Thisset)

#Note: Sets are unordered, so you cannot be sure in which order the items will appear.
#Unordered means that the items in a set do not have a defined order.
#Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#Set items are unchangeable, meaning that we cannot change the items after the set has been created.
#Once a set is created, you cannot change its items, but you can remove items and add new items.
#Duplicates Not Allowed
#Sets cannot have two items with the same value.
#To determine how many items a set has, use the len() function.
#Set items can be of any data type.
#A set can contain different data types.

#From Python's perspective, sets are defined as objects with the data type 'set':
myset = {"apple", "banana", "cherry"}
print(type(myset))

#you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

#Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Once a set is created, you cannot change its items, but you can add new items.
#Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#To add items from another set into the current set, use the update() method.
#Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
#Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset

#You can loop through the set items by using a for loop:

#There are several ways to join two or more sets in Python.
#You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#Method	                        Description
#add()	                        Adds an element to the set
#clear()                        Removes all the elements from the set
#copy()	                        Returns a copy of the set
#difference()	                  Returns a set containing the difference between two or more sets
#difference_update()	          Removes the items in this set that are also included in another, specified set
#discard()	                    Remove the specified item
#intersection()	                Returns a set, that is the intersection of two other sets
#intersection_update()	        Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	                  Returns whether two sets have a intersection or not
#issubset()	                    Returns whether another set contains this set or not
#issuperset()	                  Returns whether this set contains another set or not
#pop()	                        Removes an element from the set
#remove()	                      Removes the specified element
#symmetric_difference()	        Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	                      Return a set containing the union of sets
#update()	                      Update the set with the union of this set and others

#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Create and print a dictionary:
#1st method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#2nd metod:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

#Dictionary Items
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

#Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Duplicates Not Allowed
#Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Print the number of items in the dictionary:
print(len(thisdict))

#The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

#You can access the items of a dictionary by referring to its key name, inside square brackets:
#Get the value of the "model" key:
#1st method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
#2nd method:
x = thisdict.get("model")

#The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()
print(x)

#The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
#Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

#The values() method will return a list of all the values in the dictionary.
x = thisdict.values()
print(x)

#he list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
#Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change

#Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
car["color"] = "red"
print(x) #after the change

#The items() method will return each item in a dictionary, as tuples in a list.
x = thisdict.items()
print(x)

#To determine if a specified key is present in a dictionary use the in keyword:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#To change the Items in dictonries:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#To update Items in dictonries:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Adding an item to the dictionary is done by using a new index key and assigning a value to it:
#1st method 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#2nd method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict

#The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#Print all key names in the dictionary, one by one:
# 1st method:
for x in thisdict:
  print(x)
# 2nd method:
#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
  print(x)

#Print all values in the dictionary, one by one:
#1st method:
for x in thisdict:
  print(thisdict[x])
#2nd method:
# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
  print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
  print(x, y)

#You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#A dictionary can contain dictionaries, this is called nested dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
#Or, if you want to add three dictionaries into a new dictionary:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])

#Dictionary Methods

#Method	        Description
#clear()	      Removes all the elements from the dictionary
#copy()	        Returns a copy of the dictionary
#fromkeys()	    Returns a dictionary with the specified keys and value
#get()	        Returns the value of the specified key
#items()	      Returns a list containing a tuple for each key value pair
#keys()	        Returns a list containing the dictionary's keys
#pop()	        Removes the element with the specified key
#popitem()	    Removes the last inserted key-value pair
#setdefault()   Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#update()       Updates the dictionary with the specified key-value pairs
#values()       Returns a list of all the values in the dictionary

#if else is same as c But we there is an additions:
#elif is same as else if in c;

#One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
  pass

#while loop in python is same as in c but with the addition:
#With the continue statement we can stop the current iteration, and continue with the next;
#With the else statement we can run a block of code once when the condition no longer is true:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#for loop is same as in c but with The addition:
#Break the loop when x is 3, and see what happens with the else block;
#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3);
#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6);
#With the continue statement we can stop the current iteration of the loop, and continue with the next;
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

#Creating a Function
#In Python a function is defined using the def keyword:
def my_function():
  print("Hello from a function")
#To call it:
my_function()
#Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Emil", "Refsnes")

#Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

#Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")

#Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
#To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

#function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def myfunction():
  pass

#The Recursion in python is same as in c;

#A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression
#Syntax
# lambda arguments : expression
#Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
#Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

#Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#Use lambda functions when an anonymous function is required for a short period of time.

#You can use the append() method to add an element to an array.
cars = ["laib"]
# Add one more element to the cars array:
cars.append("Honda")

# Method	      Description
# append()	    Adds an element at the end of the list
# clear()	      Removes all the elements from the list
# copy()	      Returns a copy of the list
# count()	      Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	      Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	      Sorts the list

#Create a class named MyClass, with a property named x:
class MyClass:
  x = 5
#Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

#The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#Note: The __init__() function is called automatically every time the class is being used to create a new object.
#The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:
# The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)

# Objects can also contain methods. Methods in objects are functions that belong to the object.
# Let us create a method in the Person class:
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc()

#The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties
# You can modify properties on objects like this:
# Set the age of p1 to 40:
p1.age = 40

#Delete Object Properties
# You can delete properties on objects by using the del keyword:
# Delete the age property from the p1 object:
del p1.age

#Delete Objects
# You can delete objects by using the del keyword:
# Delete the p1 object:
del p1

#The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass

# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.
# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:
# ExampleGet your own Python Server
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
# Create a Child Class
# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
# Now the Student class has the same properties and methods as the Person class.
# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() Function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword).# 
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# Add the __init__() function to the Student class:
# class student(Person):
#   def __init__(self, fname, lname):
#     #add properties etc.

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.
# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
  
# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
# Use the super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent. 
# Add Properties
# Add a property called graduationyear to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

# In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:
# Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)

# Add Methods
# Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

#Python Iterators
# Python Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator: 
#Get your own Python Server
# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator:
# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
# We can also use a for loop to iterate through an iterable object:
# Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
# Iterate the characters of a string:
mystr = "banana"
for x in mystr:
  print(x)

# The for loop actually creates an iterator object and executes the next() method for each loop.
# Create an Iterator
# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(), which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
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
StopIteration

# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.
# To prevent the iteration from going on forever, we can use the StopIteration statement.
# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:
# Stop after 20 iterations:
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)




#The global scope Empower us for use The local value with any function;
#The modele in python use same as in c and the synthex:
# 1st method
#import name of file 
#print(name of file.value)
# 2nd method:
#import name of file as name of struct 
#print(name of file.value)





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
#By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
#Note: You cannot remove items in a tuple.
#Note: Set items are unchangeable, but you can remove items and add new items.
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
#Note: If the item to remove does not exist, remove() will raise an error.
#Note: If the item to remove does not exist, discard() will NOT raise an error.
#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
#Note: Both union() and update() will exclude any duplicate items.
#Note: The values True and 1 are considered the same value in sets, and are treated as duplicates;
#Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.