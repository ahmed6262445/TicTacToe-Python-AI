# def best_move(game):
#     move = []

#     board_length = len(game.board)

#     for i in range(board_length):
#         for j in range(board_length):
#             if game.is_valid_move(i,j):
#                 game.board[i][j] = game.player_2
#                 result = breadth_first_search(game)
#                 game.board[i][j] = ' '
#                 if result != None:
#                     move = [i,j]
#                 else:
#                     move = [i,j]
#     return move

# from copy import deepcopy
# from queue import Queue
# def breadth_first_search(game):
#     queue = Queue()
#     # visited  = []
#     queue.put(deepcopy(game))
#     board_length = len(game.board)
#     # is_maximizing = False
#     result = None

#     while not queue.empty():
#         node = deepcopy(queue.get())

#         result = node.check_winner()
#         if result != None:
#             return result

#         for i in range(board_length):
#             for j in range(board_length):  
#                 if node.is_valid_move(i,j):
#                     depth = cal_depth(node.board)
#                     if depth%2 == 0:
#                         node.board[i][j] = game.player_2
#                     else:             
#                         node.board[i][j] = game.player_1
#                     queue.put(deepcopy(node))
#                     # result = node.check_winner()
#                     # if result == 'tie':
#                     #     return result
#                     node.board[i][j] = ' '
#     return None

# def cal_depth(board):
#     count = 0 
#     board_length = len(board)
#     for i in range(board_length):
#         for j in range(board_length):
#             if board[i][j] != ' ':
#                 count += 1
#     return count 



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
    # last_result = 'O'
    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = game.player_2
                result,steps = breadth_first_search(game,i,j)
                game.board[i][j] = ' '
                if (result == game.player_2 or result == 'tie') and (steps < no_step):
                    move = [i,j]
                    no_step = steps
                    # last_result = result
                elif steps < no_step:
                    move = [i,j]
            # if game.board[i][j] == game.player_2:
            #     move = depth_first_search(game,i ,j)
    

    return move
from copy import deepcopy
from queue import Queue
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0 , 0, 1, -1, -1, 1, 1, -1]
def breadth_first_search(game,x,y):
    board_length = len(game.board)
    is_maximizing = False

    nodes_queue = Queue()
    is_maximizing_queue = Queue()
    steps_queue = Queue()

    steps = 0

    nodes_queue.put(deepcopy(game))
    is_maximizing_queue.put(is_maximizing)
    steps_queue.put(steps)

    while not nodes_queue.empty():
        node = deepcopy(nodes_queue.get())
        is_maximizing = is_maximizing_queue.get()
        steps = steps_queue.get()
        
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
                    is_maximizing_queue.put(False)
                else:
                    node.board[x_position][y_position] = node.player_1
                    is_maximizing_queue.put(True)
                nodes_queue.put(deepcopy(node))
                steps_queue.put(steps)
                node.board[x_position][y_position] = ' '
            else:
                x_position,y_position = find_source(node.board, ' ')
                if is_maximizing:
                    node.board[x_position][y_position] = node.player_2
                    steps += 1
                    is_maximizing_queue.put(False)
                else:
                    node.board[x_position][y_position] = node.player_1
                    is_maximizing_queue.put(True)
                nodes_queue.put(deepcopy(node))
                steps_queue.put(steps)
                node.board[x_position][y_position] = ' '
        # Turn shuffling between O and X
        # if is_maximizing:
        #     is_maximizing = False
        # else:
        #     is_maximizing = True
    return result,steps

def find_source(board,target):
    board_length = len(board)
    for i in range(board_length):
        for j in range(board_length):
            if board[i][j] == target:
                return [i,j]
    return []