class TicTacToe():
    def __init__(self):
        self.board = [
            ['x','o','x'],
            ['o','x','o'],
            ['o','x','x']
        ]
    
    def print_board(self):
        board = ""
        for i in range(3):
            for j in range(3):
                board += self.board[i][j]
                board += " | "
            board += "\n"
        return board



obj = TicTacToe()
print( obj.print_board())