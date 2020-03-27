from tic_tac_toe import TicTacToe
# def best_move(game):
#     move = []

#     board_length = len(game.board)

#     for i in range(board_length):
#         for j in range(board_length):
#             if game.is_valid_move(i,j):
#                 game.board[i][j] = game.player_2
#                 result = depth_first_search(game, 0, False)
#                 game.board[i][j] = ' '

#                 if result == 'tie' or result == game.player_2:
#                     move = [i,j]
#                     # break
#     return move

# def depth_first_search(game, depth, is_maximizing):
#     result = game.check_winner()
#     board_length = len(game.board)

#     if result != None:
#         return result

#     for i in range(board_length):
#         for j in range(board_length):
#             if game.is_valid_move(i,j):
#                 if is_maximizing:
#                     game.board[i][j] = game.player_2
#                     result = depth_first_search(game, depth+1, False)
#                     game.board[i][j] = ' '
#                 else:
#                     game.board[i][j] = game.player_1
#                     result = depth_first_search(game, depth+1, True)
#                     game.board[i][j] = ' '
# def best_move(game):
#     move = []

#     board_length = len(game.board)

#     for i in range(board_length):
#         for j in range(board_length):
#             if game.is_valid_move(i,j):
#                 game.board[i][j] = game.player_2
#                 result = breadth_first_search(game)
#                 game.board[i][j] = ' '
#                 if result == 'tie' or result == game.player_2:
#                     move = [i,j]
#                     # return move
#     return move

def best_move(game):
    move = []

    board_length = len(game.board)
    result = None
    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = game.player_2
                result = breadth_first_search(game)
                game.board[i][j] = ' '
                if result == 'tie' or result == game.player_2:
                    move = [i,j]
                    return move
                elif result == game.player_1:
                    move = [i,j] 
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

obj = TicTacToe()

# obj.board[0][0] = 'O'
# obj.board[2][1] = 'X'
# obj.board[0][1] = 'O'
# obj.board[0][2] = 'X'
# obj.board[1][0] = 'O'
# obj.board[2][0] = 'X'
obj.board[0][0] = 'O'
obj.board[0][1] = 'O'
obj.board[2][2] = 'X'
obj.board[0][2] = 'X'

print(obj.print_board())
move=best_move(obj)
print(move)
# new_obj = breadth_first_search(obj)

# print(new_obj.print_board())