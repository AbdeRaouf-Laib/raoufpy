

def num_player():
    number_player = input("How many players?")
    return number_player
def F_start_game():
    numberof_player = num_player()
    if numberof_player == 1:
        print("1")
        print("laib")
    print("do you have get up")
        

def main():
    print("Hay ,welcome To Dice game")
    print("are you ready")
    start_value = input("press 's' :")
    if start_value == 's' or start_value == 'S':
        F_start_game()
    else:
        print("Do you want to exit the application?")
        end_value = input("Press 'y' to exit or any Key To repeat:")
        if end_value != 'y':
            main()
        else:
            return

main()