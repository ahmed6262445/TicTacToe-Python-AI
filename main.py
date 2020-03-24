from tic_tac_toe import TicTacToe
from os import system
import getch as inp
from time import sleep
clear = lambda: system('clear')

player_1 = 'O'
player_2 = 'X'
plays_first = 'O'

clear()
print("Loading...")
sleep(1)
while True:
    clear()
    print("Tic Tac Toe\n1) Start Game\n2) Settings\n3) Exit")
    main_input = inp.getch()

    if main_input == '1':
        print("Loading...")
        sleep(1)
        tictactoe = TicTacToe(player_1=player_1, player_2=player_2, last_player=plays_first)
        
        help_board = False

        tictactoe.shift_player()
        plays_first = tictactoe.get_current_player()
        tictactoe.shift_player()

        player_before_shift = tictactoe.get_current_player()
        while True:
            clear()
            print("Tic Tac Toe\nEnter 'q' to quit the game.\nEnter 'h' to print help board.\n")
            if help_board:
                print(tictactoe.print_hint_board())
            print (tictactoe.print_board())

            print(f"Player 1 = {player_1}\tPlayer 2 = {player_2}")
            print(f"{tictactoe.get_current_player()}'s Turn")
            game_input = input('Enter value from 1-9: ')

            if game_input == 'q':
                print("Quiting game...")
                sleep(2)
                break
            elif game_input == 'h':
                if help_board == True:
                    help_board = False
                else:
                    help_board = True
                continue
            elif game_input == '' or len(game_input) > 1 or (ord(game_input) < ord('1') or ord(game_input) > ord('9')) :
                print("Invalide input...")
                sleep(1)
                continue
            else:
                if tictactoe.get_move(int(game_input)):
                    tictactoe.make_move()
                else:
                    print("Place alreay occupied...")
                    sleep(1)

            player_before_shift = tictactoe.get_current_player()
            if tictactoe.win_game():
                clear()
                print(f"Tic Tac Toe\n\n{tictactoe.print_board()}")
                print(f"Player {player_before_shift} Won")
                break
            elif tictactoe.game_draw():
                print(f"Game is draw.")
                break
            tictactoe.shift_player()
        # Game While Loop Ends
        print("Press Enter to continue...")
        while True:
            if ord(inp.getch()) == 10:
                break
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
                break #breaks Setings While Loop
        # Settings While Loop ends
    elif main_input == '3':
        clear()
        exit()
# Main While Loop ends