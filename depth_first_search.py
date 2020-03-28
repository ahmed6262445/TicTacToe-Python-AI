from tic_tac_toe import TicTacToe
# def best_move(game):
#     move = []
#     result = None
#     board_length = len(game.board)

    # for i in range(board_length):
    #     for j in range(board_length):
    #         if game.is_valid_move(i,j):
    #             game.board[i][j] = game.player_2
    #             result = depth_first_search(game)
    #             game.board[i][j] = ' '
    #             if result != None:
    #                 move = [i,j]
#     return move

# from copy import deepcopy
# def depth_first_search(game):
#     stack = []
#     stack.append(deepcopy(game))
#     board_length = len(game.board)
#     is_maximizing = False
#     while len(stack) != 0:
#         node = deepcopy(stack.pop())
#         result = node.check_winner()
#         if result != None:
#             return result
#         for i in range(board_length): # Creating State Space or adding child(neigboring) nodes 
#             for j in range(board_length):
#                 if node.is_valid_move(i,j):
#                     if is_maximizing:
#                         node.board[i][j] = node.player_2
#                     else:
#                         node.board[i][j] = node.player_1
#                     stack.append(deepcopy(node))
#                     # result = node.check_winner()
#                     # if result == node.player_2:
#                     #     return result
#                     node.board[i][j] = ' '
#         if is_maximizing:
#             is_maximizing = False
#         else:
#             is_maximizing = True
#     return result
from random import randrange
def best_move(game):
    """
    Returns a list of x and y co-ordinates of the move
    """
    if game.is_empty():
        return [1,1]
    if game.board[1][1] == ' ':
        return [1,1]
    
    move = []
    board_length = len(game.board)
    no_step = float('inf') # to track no of steps taken to acheive a goal
    steps = float('inf')
    last_result = 'O'
    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = game.player_2
                result,steps = depth_first_search(game,i,j)
                game.board[i][j] = ' '
                if (result == game.player_2 or result == 'tie') and (steps < no_step):
                    move = [i,j]
                    no_step = steps
                    last_result = result
                elif steps < no_step:
                    move = [i,j]
            # if game.board[i][j] == game.player_2:
            #     move = depth_first_search(game,i ,j)
    

    return move
from copy import deepcopy

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0 , 0, 1, -1, -1, 1, 1, -1]
def depth_first_search(game,x,y):
    board_length = len(game.board)
    is_maximizing = False
    move = []
    nodes_stack = []
    moves_stack = []
    steps = 0
    nodes_stack.append(deepcopy(game))
    moves_stack.append([x,y])

    while len(nodes_stack) != 0:
        node = deepcopy(nodes_stack.pop())
        move = moves_stack.pop()

        result = node.check_winner()
        if result != None: #result == node.player_2 or result == 'tie':
            return [result,steps]
        source = []
        if is_maximizing:
            source = find_source(node.board, node.player_2)
        else:
            source = find_source(node.board, node.player_1)
        
        x_position = -1
        y_position = -1
        # Checking neighboring Nodes
        for i in range(len(dr)):
            if len(source) != 0:
                x_position = (source[0] + dr[i])
                y_position = (source[1] + dc[i])
            else:
                x_position,y_position = find_source(node.board, ' ')

            if x_position < 0 or y_position < 0 or x_position == board_length or y_position == board_length:
                continue

            if node.is_valid_move(x_position,y_position):
                if is_maximizing:
                    node.board[x_position][y_position] = node.player_2
                    steps += 1
                else:
                    node.board[x_position][y_position] = node.player_1
                nodes_stack.append(deepcopy(node))
                moves_stack.append([x_position,y_position])
                node.board[x_position][y_position] = ' '
            else:
                x_position,y_position = find_source(node.board, ' ')
                if is_maximizing:
                    node.board[x_position][y_position] = node.player_2
                    steps += 1
                else:
                        node.board[x_position][y_position] = node.player_1
                nodes_stack.append(deepcopy(node))
                moves_stack.append([x_position,y_position])
                node.board[x_position][y_position] = ' '
        # Turn shuffling between O and X
        if is_maximizing:
            is_maximizing = False
        else:
            is_maximizing = True
    return result,steps

def find_source(board,target):
    board_length = len(board)
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == target:
                return [i,j]
    return []






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