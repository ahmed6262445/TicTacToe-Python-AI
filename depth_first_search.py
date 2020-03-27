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
def best_move(game):
    move = []

    board_length = len(game.board)

    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = game.player_2
                result = depth_first_search(game)
                game.board[i][j] = ' '
                if result != None:
                    move = [i,j]
                # return move
    return move

from copy import deepcopy
def depth_first_search(game):
    stack = []
    stack.append(deepcopy(game))
    board_length = len(game.board)
    is_maximizing = False
    while len(stack) != 0:
        node = deepcopy(stack.pop())

        result = node.check_winner()
        if result != None:
            return result

        for i in range(board_length):
            for j in range(board_length):
                if node.is_valid_move(i,j):
                    if is_maximizing:
                        node.board[i][j] = node.player_2
                    else:
                        node.board[i][j] = node.player_1
                    stack.append(deepcopy(node))
                    node.board[i][j] = ' '
        if is_maximizing:
            is_maximizing = False
        else:
            is_maximizing = True
    return result

obj = TicTacToe()

# # obj.board[0][0] = 'O'
# # obj.board[2][1] = 'X'
# # obj.board[0][1] = 'O'
# # obj.board[0][2] = 'X'
# # obj.board[1][0] = 'O'
# # obj.board[2][0] = 'X'
# obj.board[0][0] = 'O'
# obj.board[0][1] = 'O'
# obj.board[2][2] = 'X'
# obj.board[0][2] = 'X'

# print(obj.print_board())
# move=best_move(obj)
# print(move)
# # new_obj = breadth_first_search(obj)

# # print(new_obj.print_board())