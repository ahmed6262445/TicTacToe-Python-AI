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
    return result
