# #1st exo:
# largeur = 20
# hauteur = 5 * 9.3 
# print(largeur * hauteur) # = 930
# #2nd exo:
# a,b,c = 3,5,7
# print(b // c)
# print(a - b // c) #3 because // is first than - and b // c = 0 
# #3ed exo:
# r , pi = 12 , 3.14159
# s = pi * r**2
# print(s) #print the result of pi * r**2
# print(type(r),type(pi),type(s)) #print the type of varible 
# #4th exo:
# #1st method
# a , c = 3 , 5
# b = a
# a = c
# c = b
# print(a,c)
# #2nd method
# d , e = 3 , 5
# e , d = d , e
# print(e , d)
# #5th exo:
# #1st:  
# a = 0
# i = 0
# while a < 20:
#     a = a + 1
#     i = a * 7
#     print(a , i)
# #2nd:
# Dollar = 0
# i = 0
# Euro = int(input("How much Euro:"))
# while i < Euro:
#     i += 1
#     Dollar += 1.65
# print(Euro ,"Euro is ", Dollar,"Dollar")
# #6th:
# Length = int(input("Enter the length of Cuboid: ")) 
# width = int(input("Enter The width of Cubiod: "))
# height = int(input("Enter The height of cubiod: "))
# area = (Length * width) * 2 + (width * height) * 2 + (Length * height) * 2
# print("The area of cubiod is: ",area," cm3")
# #7th:
# Seconds = int(input("Enter the number of Seconds: "))
# year = Seconds / 31536000
# month = (Seconds % 31536000) / 2592000
# day = ((Seconds % 31536000) % 2592000) / 86400
# print(int(year) ,"y " , int(month), "m " , int(day),"d " ,int(((Seconds % 31536000) % 2592000) % 86.400),"s")
# #8th exo:
# a = 1
# i = 1
# while i < 20:
#     a = i * 7
#     i += 1
#     if (a % 3) == 0:
#         print("*",end="")
#     print(a,end=" ")
#9th exo:
# radians = int(input("""Enter the """))
# degree = radians * 180
# min = (radians % 180) * 60
# sec = ((radians % 180) % 60) * 60
# print("degree: ", degree ,"min: ",min ,"second", sec)

file = open("text.txt", "a")
file.write("Hello i am laib abderaouf")
file.close()

openfile = open("text.txt" ,"r")
print(openfile.read())