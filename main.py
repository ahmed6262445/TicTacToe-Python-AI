from tic_tac_toe import TicTacToe
from os import system
from time import sleep
import colors
import platform
from os import system
from mini_max import *
from random import randrange

os_name = platform.system().lower()

if 'windows' in os_name:
    try:
        import msvcrt as inp
    except ImportError as e:
        print(e)
        exit()
else:
    try:
        import getch as inp
    except ImportError as e:
        print(e)
        exit()

def clear():
    """
    Clears the console
    """
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def get_input():
    """
    Gets instant input from the console
    """
    if 'windows' in os_name:
        return inp.getch().decode('ASCII')
    else:
        return inp.getch()

def player_input_checks(game_input):
    pass
    

plays_first = 'X'
clear()
print("Loading...")
sleep(1)
while True:
    clear()
    print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n1) {colors.underline}Start Game{colors.reset}\n2) {colors.underline}Exit{colors.reset}")
    main_input = get_input()

    if main_input == '1':
        print(f"{colors.fg.blue}Loading...{colors.reset}")
        sleep(1)
        tictactoe = TicTacToe(last_player=plays_first)
        help_board = False

        tictactoe.shift_player()
        plays_first = tictactoe.current_player
        tictactoe.shift_player()

        clear()
        print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n1) {colors.underline}Play with another player{colors.reset}\n2) {colors.underline}Play with AI{colors.reset}")

        is_ai = False
        ai_turn = False
        while True:
            ai_choice = get_input()

            if ai_choice == '1':
                break
            elif ai_choice == '2':
                is_ai = True
                # if tictactoe.current_player == tictactoe.player_2:
                #     ai_turn = True
                break 
        # ai choice loop Ends

        clear()
        if not is_ai:
            print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n {colors.underline}Player 1 goes first or Player 2 (1/2){colors.reset}")
        else:
            print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n {colors.underline}Player 1 goes first or Player 2 (AI) (1/2){colors.reset}")
        while True:
            goes_first = get_input()

            if goes_first == '1':
                tictactoe.current_player = tictactoe.player_1
                break
            elif goes_first == '2':
                tictactoe.current_player = tictactoe.player_2
                if is_ai:
                    ai_turn = True
                break
        # Goes first choice Loop Ends
        while True:

            clear()
            print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n{colors.fg.blue}Enter 'q' to quit the game.\nEnter 'h' to print help board.{colors.reset}\n")

            if help_board:
                print(f"{colors.fg.blue}{tictactoe.print_hint_board()}{colors.reset}")
            print (tictactoe.print_board())

            winner = tictactoe.check_winner()
            if winner == 'tie':
                print(f"\n{colors.bold}{colors.underline}Game is a TIE!")
                break
            elif winner == tictactoe.player_1:
                print(f"{colors.bold}{colors.underline}{colors.fg.green}Player 1 ({tictactoe.player_1}) Won{colors.reset}")
                break
            elif winner == tictactoe.player_2:
                print(f"{colors.bold}{colors.underline}{colors.fg.green}Player 2 ({tictactoe.player_2}) Won{colors.reset}")
                break

            if tictactoe.current_player == tictactoe.player_1:
                print(f"{colors.bold}{colors.underline}{colors.bg.red}Player 1 = {tictactoe.player_1} {colors.reset}\tPlayer 2 = {tictactoe.player_2}")
            else:
                print(f"Player 1 = {tictactoe.player_1}\t{colors.bold}{colors.underline}{colors.bg.red}Player 2 = {tictactoe.player_2} {colors.reset}")
            print(f"\n{colors.underline}{tictactoe.current_player}'s Turn to play'{colors.reset}")

            if ai_turn == False:
                game_input = input(f"{colors.bold}{colors.underline}Please select input (1-9):{colors.reset} ")

                if game_input == 'q':
                    print(f"{colors.fg.red}Quiting game...{colors.reset}")
                    sleep(2)
                    break # Breaks Game Loop
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

                if tictactoe.set_move(int(game_input)):
                    tictactoe.make_move()
                    tictactoe.shift_player()

                    winner = tictactoe.check_winner()
                    if winner == tictactoe.player_1 or winner == 'tie':
                        continue
                else:
                    print(f"Place Already Occupied")
                    sleep(1)
                    continue

                if is_ai:
                    ai_turn = True

            if is_ai:
                while True:
                    # ai_move = randrange(1,9)
                    ai_move = best_move(tictactoe)
                    if tictactoe.is_valid_move(ai_move[0],ai_move[1]):
                        tictactoe.board[ai_move[0]][ai_move[1]] = tictactoe.player_2
                        tictactoe.shift_player()
                        ai_turn = False
                        break
                # AI Move Loop Ends

        # Game While Loop Ends
        print("Press Enter to continue...")
    # Choice '1' If Ends
        while True:
            i = get_input()
            if i == '\r' or i == '\n':
                break
    elif main_input == '2':
        clear()
        exit()
# Main While Loop ends