from tic_tac_toe import TicTacToe
from os import system
from time import sleep
import colors
# import getch as inp
import platform
from adjacency_matrix_graph import AdjacencyMatrixGraph
from depth_first_search import *
from breadth_first_search import *
from os import system

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
        return get_input()
    else:
        return inp.getch()

graph = AdjacencyMatrixGraph(9)

graph.add_edge(0,1)
graph.add_edge(0,3)
graph.add_edge(0,4)

graph.add_edge(1,2)
graph.add_edge(1,4)

graph.add_edge(2,4)
graph.add_edge(2,5)

graph.add_edge(3,4)
graph.add_edge(3,6)

graph.add_edge(4,5)
graph.add_edge(4,6)
graph.add_edge(4,7)
graph.add_edge(4,8)

graph.add_edge(5,8)

graph.add_edge(6,7)

graph.add_edge(7,8)

# depth_first(graph)
# print("Breadth First Search")
# breadth_first(graph)
# exit()

player_1 = 'O'
player_2 = 'X'
plays_first = 'O'
clear()
print("Loading...")
sleep(1)
while True:
    clear()
    print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n1) {colors.underline}Start Game{colors.reset}\n2) {colors.underline}Settings{colors.reset}\n3) {colors.underline}Exit{colors.reset}")
    main_input = get_input()

    if main_input == '1':
        print(f"{colors.fg.blue}Loading...{colors.reset}")
        sleep(1)
        tictactoe = TicTacToe(player_1=player_1, player_2=player_2, last_player=plays_first)
        
        help_board = False

        tictactoe.shift_player()
        plays_first = tictactoe.get_current_player()
        tictactoe.shift_player()

        player_before_shift = tictactoe.get_current_player()
        while True:
            clear()
            print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n{colors.fg.blue}Enter 'q' to quit the game.\nEnter 'h' to print help board.{colors.reset}\n")
            if help_board:
                print(f"{colors.fg.blue}{tictactoe.print_hint_board()}{colors.reset}")
            print (tictactoe.print_board())

            if tictactoe.get_current_player() == tictactoe.player_1:
                print(f"{colors.bold}{colors.bg.red}{colors.underline}Player 1 = {player_1}{colors.reset}\tPlayer 2 = {player_2}")
            else:
                print(f"Player 1 = {player_1}{colors.bold}{colors.bg.red}\tPlayer 2 = {player_2}{colors.reset}")
            print(f"\n{tictactoe.get_current_player()}'s Turn")
            game_input = input(f"{colors.bold}{colors.underline}Enter value from 1-9:{colors.reset} ")

            if game_input == 'q':
                print(f"{colors.fg.red}Quiting game...{colors.reset}")
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
                    continue

            player_before_shift = tictactoe.get_current_player()
            if tictactoe.win_game():
                clear()
                print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n{tictactoe.print_board()}")
                print(f"Player {player_before_shift} Won")
                break
            elif tictactoe.game_draw():
                clear()
                print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\n{tictactoe.print_board()}")
                print(f"Game is draw.")
                break
            tictactoe.shift_player()
        # Game While Loop Ends
        print("Press Enter to continue...")
        while True:
            if ord(get_input()) == 10:
                break
    elif main_input == '2':
        while True:
            clear()
            print(f"{colors.bold}{colors.underline}Tic Tac Toe{colors.reset}\n\nSettings\n1) Change Symbols\n\tPlayer 1 = {player_1}\n\tPlayer 2 = {player_2}\n2) Go Back")
            setting_input = get_input()
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