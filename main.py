import os
from game import Game
from time import sleep
from classes import Team
import addcards


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
            file = open("Instructions.txt", "r")
            for line in file:
                print(line)
                sleep(1)
            file.close()
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

            if isinstance(winner, str):
                print(winner)
                print("Thanks for playing!")
                input("Press enter to continue to main menu: ")
                clear_screen()
            else:
                print(f"The winner is {winner.name}!")
                print("Thanks for playing!")
                input("Press enter to continue to main menu: ")
                clear_screen()
                continue

        elif choice == "3":
            clear_screen()
            addcards.add_card()
            sleep(1.5)
            clear_screen()
            continue
        else:
            print("Sorry, wrong input, try again!")
            sleep(1.5)
            clear_screen()
            continue

#if __name__ == '__main__':
#   main()
