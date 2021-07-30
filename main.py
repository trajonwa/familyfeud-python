import os
from game import Game
from time import sleep, time
from classes import Team

def clear_screen():
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            _ = os.system('cls')

def main():
    while True:
        print("Welcome to Family Feud!")
        print("Type a number for what you would like to do!")
        print("1. View Instructions")
        print("2. Play the Game!")
        print("3. Add New Cards")
        choice = input("Enter your choice: ")

        if choice == "1":
            # print instructions:
            input("Press enter to continue: ")
            clear_screen()
            continue
        elif choice == "2":
            print("Let's play!")

            sleep(2)
            clear_screen()

            first_team = Team(input("Team 1, Enter your name here: "))
            second_team = Team(input("Team 2, Enter your name here: "))
            game = Game(first_team, second_team)
            winner = game.play(first_team, second_team)

            if winner is str():
                print(winner)
                print("Thanks for playing!")
            else:
                print(f"The winner is {winner}!")
                print("Thanks for playing!")

        elif choice == "3":
            # Add card function here
            sleep(1.5)
            clear_screen()
            continue
        else:
            print("Sorry, wrong input, try again!")
            sleep(1.5)
            clear_screen()
            continue

if __name__ == '__main__':
    main()
