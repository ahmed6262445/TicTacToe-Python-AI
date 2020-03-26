from tic_tac_toe import TicTacToe
def best_move(game):
    move = []

    board_length = len(game.board)

    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = game.player_2
                result = depth_first_search(game, 0, False)
                game.board[i][j] = ' '

                if result == 'tie' or result == game.player_2:
                    move = [i,j]
                    # break
    return move

def depth_first_search(game, depth, is_maximizing):
    result = game.check_winner()
    board_length = len(game.board)

    if result != None:
        return result

    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                if is_maximizing:
                    game.board[i][j] = game.player_2
                    result = depth_first_search(game, depth+1, False)
                    game.board[i][j] = ' '
                else:
                    game.board[i][j] = game.player_1
                    result = depth_first_search(game, depth+1, True)
                    game.board[i][j] = ' '

from queue import Queue
import numpy as ns
from copy import deepcopy
def breadth_first_search(game):
    queue = Queue()
    visited  = []
    queue.put(deepcopy(game))
    board_length = len(game.board)
    is_maximizing = False

    while not queue.empty():
        node = deepcopy(queue.get())

        result = node.check_winner()
        if result == node.player_2 or result == 'tie':
            return node

        for i in range(3):
            for j in range(3):  
                if node.is_valid_move(i,j):
                    if is_maximizing:
                        node.board[i][j] = game.player_2
                    else:             
                        node.board[i][j] = game.player_1
                    queue.put(deepcopy(node))
                    node.board[i][j] = ' '
        if is_maximizing:
            is_maximizing = False
        else:
            is_maximizing = True
        

obj = TicTacToe()
obj.board[0][0] = obj.player_1
obj.board[0][1] = obj.player_2

new_obj = breadth_first_search(obj)

print(new_obj.print_board())