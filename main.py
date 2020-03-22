from tic_tac_toe import TicTacToe
from os import system
import getch as input
from time import sleep
clear = lambda: system('clear')

player_1 = 'O'
player_2 = 'X'
while True:
    clear()
    print("Tic Tac Toe\n1) Start Game\n2)Settings\n3)Exit")
    main_input = input.getch()
    

    if main_input == '1':
        pass
    elif main_input == '2':
        while True:
            clear()
            print(f"Tic Tac Toe\nSettings\n1)Change Symbols\n\tPlayer 1 = {player_1}\n\tPlayer 2 = {player_2}\n2) Go Back")
            setting_input = input.getch()
            if setting_input == '1':
                temp = player_1
                player_1 = player_2
                player_2 = temp
                print("Changing symbols...")
                sleep(2)
                print("Symbols changed successfully.")
                sleep(1)
            elif setting_input == '2':
                break #breaks Seetings While Loop
        # Settings While Loop ends
    elif main_input == '3':
        clear()
        exit()
# Main While Loop ends