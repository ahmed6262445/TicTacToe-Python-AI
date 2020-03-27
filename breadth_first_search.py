def best_move(game):
    move = []

    board_length = len(game.board)

    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = game.player_2
                result = breadth_first_search(game)
                game.board[i][j] = ' '
                if result == 'tie' or result == game.player_2:
                    move = [i,j]
                    return move
    return move

from copy import deepcopy
from queue import Queue
def breadth_first_search(game):
    queue = Queue()
    # visited  = []
    queue.put(deepcopy(game))
    board_length = len(game.board)
    is_maximizing = False
    while not queue.empty():
        node = deepcopy(queue.get())

        result = node.check_winner()
        if result != None:
            return result

        for i in range(board_length):
            for j in range(board_length):  
                if node.is_valid_move(i,j):
                    depth = cal_depth(node.board)
                    if depth%2 == 0:
                        node.board[i][j] = game.player_2
                    else:             
                        node.board[i][j] = game.player_1
                    queue.put(deepcopy(node))
                    node.board[i][j] = ' '

def cal_depth(board):
    count = 0 
    board_length = len(board)
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] != ' ':
                count += 1
    return count 
