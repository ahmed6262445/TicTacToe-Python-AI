def best_move(game):
    """
        Parameter: game (reference of the original game board)
        Return: Returns 'x' and 'y' co-ordinated for best move
    """
    best_score = -float('inf')
    move = []
    board_length = len(game.board)

    for i in range(board_length):
        for j in range(board_length):
            if game.is_valid_move(i,j):
                game.board[i][j] = 'O'
                score = minimax(game, 0, False)
                game.board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = [i,j]
    return move

scores = {
    'X':-10,
    'O': 10,
    'tie': 0
}

def minimax(game, depth, is_maximizing):
    result = game.check_winner()

    if result != None:
        return scores[result] 

    board_length = len(game.board)

    if is_maximizing:
        best_score = -float('inf')
        for i in range(board_length):
            for j in range(board_length):
                if game.is_valid_move(i,j):
                    game.board[i][j] = game.player_2
                    score = minimax(game, depth+1, False)
                    game.board[i][j] = ' '
                    best_score = max(score,best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(board_length):
            for j in range(board_length):
                if game.is_valid_move(i,j):
                    game.board[i][j] = game.player_1
                    score = minimax(game, depth+1, True)
                    game.board[i][j] = ' '
                    best_score = min(score,best_score)
        return best_score