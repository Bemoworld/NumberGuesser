import random
import sys

name = input("Please enter your name: ")

# MAIN MENU

def main_menu():
    print("\nHello, " + name + """

--- Main Menu ---

Press 1 to play
Press 2 to quit

""")

    menu_selection_word = input("please select your option: \n")
    try:
        menu_selection_int = int(menu_selection_word)
        print("You have selected: ", menu_selection_int)
    except ValueError:
        print("Invalid selection")
        main_menu()
    if menu_selection_int == 1:
        play_game()
    else:
        game_quit()

# GAME QUIT

def game_quit():
    os.system('clear')
    sys.exit("Thanks for playing!")

# PLAY GAME
def play_game():
    number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    target = random.choice(number)
    guess = int(input("Guess a number between 1 and 20: \n"))
    correct_answer = False
    turn = 0
    while correct_answer == False and turn < 10:
        if guess == target:
            print("Correct, " + name + ", you did it at turn " + str(turn) + "!")
            correct_answer = True
            main_menu()

        else:
            turn += 1
            if guess < target:
                print("Too low! turn: " + str(turn))
                guess = int(input("Guess a number between 1 and 20: \n"))
            elif guess > target:
                print("Too high! turn: " + str(turn))
                guess = int(input("Guess a number between 1 and 20: \n"))
    
    if correct_answer == False and turn == 10:
        print("You lost, " + name + " the number was: " + str(target))
        main_menu()

# START
main_menu()
