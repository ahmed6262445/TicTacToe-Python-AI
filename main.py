from tic_tac_toe import TicTacToe
from os import system
import getch as inp
from time import sleep
clear = lambda: system('clear')

player_1 = 'O'
player_2 = 'X'
plays_first = 'O'

while True:
    clear()
    print("Tic Tac Toe\n1) Start Game\n2) Settings\n3) Exit")
    main_input = inp.getch()
    

    if main_input == '1':
        tic_tac_toe = TicTacToe(player_1=player_1, player_2=player_2, last_player=plays_first)
        while not tic_tac_toe.game_over():
            clear()
            print("Tic Tac Toe\nEnter 'q' to quit the game.\nEnter 'h' to print help board.\n")
            print (tic_tac_toe.print_board())
            game_input = input('Enter value from 1-9: ')
            if game_input == 'q':
                print("Quiting game...")
                break
            elif game_input == '' or len(game_input) > 1 or (ord(game_input) < ord('1') or ord(game_input) > ord('9')) :
                print("Invalide input...")
                sleep(1)
                continue
        # Game While Loop Ends
        sleep(5)
    elif main_input == '2':
        while True:
            clear()
            print(f"Tic Tac Toe\nSettings\n1)Change Symbols\n\tPlayer 1 = {player_1}\n\tPlayer 2 = {player_2}\n2) Go Back")
            setting_input = inp.getch()
            if setting_input == '1':
                temp = player_1
                player_1 = player_2
                player_2 = temp
                print("Changing symbols...")
                sleep(1.5)
                print("Symbols changed successfully!")
                sleep(1.25)
            elif setting_input == '2':
                break #breaks Seetings While Loop
        # Settings While Loop ends
    elif main_input == '3':
        clear()
        exit()
# Main While Loop ends