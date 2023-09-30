#1st exo:
largeur = 20
hauteur = 5 * 9.3 
print(largeur * hauteur) # = 930
#2nd exo:
a,b,c = 3,5,7
print(b // c)
print(a - b // c) #3 because // is first than - and b // c = 0 
#3ed exo:
r , pi = 12 , 3.14159
s = pi * r**2
print(s) #print the result of pi * r**2
print(type(r),type(pi),type(s)) #print the type of varible 
#4th exo:
#1st method
a , c = 3 , 5
b = a
a = c
c = b
print(a,c)
#2nd method
d , e = 3 , 5
e , d = d , e
print(e , d)
#5th exo:
#1st:  
a = 0
i = 0
while a < 20:
    a = a + 1
    i = a * 7
    print(a , i)
#2nd:
Dollar = 0
i = 0
Euro = int(input("How much Euro:"))
while i < Euro:
    i += 1
    Dollar += 1.65
print(Euro ,"Euro is ", Dollar,"Dollar")
#3ed:
