from random import randrange

def enter_number():
    global first_number
    first_number= int(input("Enter The first Number of list (int): "))
    global last_number
    last_number= int(input("Enter the last Number of The list (int): "))
    print("",end="\n\n\n")
    global deffrent_number
    deffrent_number= last_number - first_number

Ready = input("Welcome, are you ready to start The correct Number Guessing Game? (y or yes): ")
print("",end="\n\n")



if Ready == "Y" or Ready == "YES" or Ready == "y" or Ready == "yes" or Ready == "Yes" :
    print("The game Rules:")
    print( "   -Enter only intger number.")
    print( "   -If you Enter a floating number, We will convert it to an integer.")
    print( "   -Adhering to the game`s instructions, it is important")
    print( "   -If you want to Exit game enter (e or ext) ",end="\n\n\n")

    print("start!!!!",end="\n\n\n")
    enter_number()
    if deffrent_number > 2:
        print(f"The probablity that you get the correct number is 1 OUT OF {deffrent_number}!!!" ,end="\n")
        print("Can you do it the first time",end="\n\n\n")
    else:
        print("Enter a slightly larger list!!!",end="\n\n")
        enter_number()
        
    try:
        random_number = randrange(first_number,last_number)
        i = 1
        print(f"   -Enter only The numbers with { first_number} and {last_number}:",end="\n\n")
        while 1: 
            user_number = int(input())
            try:
                if user_number < last_number or user_number > first_number :
                    if user_number != random_number:
                        i += 1
                        print("Try again!!!")
                        if user_number < random_number: 
                            print(f"Enter numbers greater than {user_number}",end="\n\n")
                        elif user_number > random_number:
                            print(f"Enter numbers smaller than {user_number}",end="\n\n")
                        else:
                            pass
                    elif user_number == random_number:
                        print("You Win!!!",end="\n\n\n")
                        
                        break
            except:
                print("wrong number.",end="\n\n")
        if i > 1:
            print(f"You succeeded afeter {i} attempts",end="\n\n")
        elif i == 1:
            print("You worked the first time, Congratulations!!!",end="\n\n")
    except:
        print("wrong nember.",end="\n\n")
else:
    print("Good bye!!!")
    pass