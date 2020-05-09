# This is a word game
import random
import time
import sys




def Quit():
    sys.exit("""Thank you for Playing!
    Hope u enjoyed it 
    Bye!""")


def Information():
    print('\nYou will have 4 categories to choose:\nSuper Heroes, Cars, Fruits and Countries.\nYou need to guess word.\nIf you made more than 6 mistakes, Game is finish and you lost.\nYou can guess 1 letter in time.\nGood Luck!')
    time.sleep(3)
    User_Selection()


def Main_Menu():
    Player = input('Unknown User, please, write your name: ')
    time.sleep(3)
    print(f'\nHello, {Player.title()}, Welcome to my HangMan Game.'
          '\nPress 1 for Game Info\nPress 2 for Play Game\nPress 3 for Quit')
    User_Selection()


def User_Selection():
    menu_selection = input("please select your option(4-Back to Menu): \n")
    try:
        menu_selection_number = int(menu_selection)
        print("you have selected: ", menu_selection_number)
    except ValueError:
        print(" Invalid selection")
        User_Selection()

    if menu_selection_number == 1:
        Information()
    elif menu_selection_number == 2:
        WordSelection()
    elif menu_selection_number == 3:
        Quit()
    elif menu_selection_number == 4:
        Main_Menu()
    else:
        print(" Invaild selection \n")
        User_Selection()


def Print_Hangman(guesses, wd):
    if guesses == 0:
        print("_________")
        print("|	 |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 1:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|")
        print("|")
        print("|")
        print("|________")
    elif guesses == 2:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	 |")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 3:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 4:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|")
        print("|________")
    elif guesses == 5:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ ")
        print("|________")
    elif guesses == 6:
        print("_________")
        print("|	 |")
        print("|	 O")
        print("|	\|/")
        print("|	 |")
        print("|	/ \ ")
        print("|________")
        print("\n")
        print("The word was %s." % wd)
        print("\n")
        print("\nYOU LOSE! TRY AGAIN!")
        print("\nWould you like to play again, type 1 for yes or 2 for no?")
        again = str(input("> "))
        again = again.lower()
        if again == "1":
            WordSelection()
        return


def WordSelection():
    SuperHeroes = ['hawkeye', 'robin', 'galactus', 'thor', 'mystique', 'superman', 'deadpool', 'vision', 'sandman',
                   'aquaman']
    Cars = ['nissan', 'porsche', 'audi', 'hyundai', 'ford', 'volkswagen', 'honda', 'bmw', 'toyota', 'mercedes']
    Fruits = ['pear', 'mango', 'apple', 'banana', 'apricot', 'pineapple', 'cantaloupe', 'grapefruit', 'jackfruit',
              'papaya']
    Countries = ['russia', 'usa', 'poland', 'canada', 'uk', 'ukraine', 'brazil', 'argentine', 'bulgaria', 'czechia']
    print("Let's play Hangman. I have 4 categories for you to select")
    print(
        '\nPress 1 for Super Heroes.\nPress 2 for Cars.\nPress 3 for Fruits.\nPress 4 for Countries\nPress 5 for Main Menu')
    inp = input('Select one option: ')
    try:
        inp_int = int(inp)
        print("you have selected: ", inp_int)
    except ValueError:
        print(" Invalid selection")
        WordSelection()
    if inp_int == 1:
        Word = random.choice(list(SuperHeroes))
    elif inp_int == 2:
        Word = random.choice(list(Cars))
    elif inp_int == 3:
        Word = random.choice(list(Fruits))
    elif inp_int == 4:
        Word = random.choice(list(Countries))
    elif inp_int == 5:
        Main_Menu()
    else:
        print("Invalid Input")
        WordSelection()

    guesses = 0
    word_list = list(Word)
    blanks = "_" * len(Word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print("Let's play hangman!\n")
    Print_Hangman(guesses, Word)
    print("\n")
    print("" + ' '.join(blanks_list))
    print("\n")
    print("Guess a letter.\n")

    while guesses < 6:
        guess = str(input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            print("Stop cheating! Enter one letter at time.")
        elif guess == "":
            print("Don't you want to play? Enter one letter at a time.")
        elif guess in guess_list:
            print("You already guessed that letter! Here is what you've guessed:")
            print(' '.join(guess_list))
        else:
            guess_list.append(guess)
            i = 0
            while i < len(Word):
                if guess == Word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print("Your letter isn't here.")
                guesses = guesses + 1
                Print_Hangman(guesses, Word)

                if guesses < 6:
                    print("Guess again.")
                    print(' '.join(blanks_list))

            elif word_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print(' '.join(blanks_list))

                if word_list == blanks_list:
                    print("\nYOU WIN! Here is your prize:")
                    print("\n")
                    print("Would you like to play again?")
                    print("Type 1 for yes or 2 for no.")
                    again = str(input("> "))
                    if again == "1":
                        WordSelection()
                    quit()

                else:
                    print("Great guess! Guess another!")


Main_Menu()