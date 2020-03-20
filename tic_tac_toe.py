import random
class TicTacToe():
    def __init__(self,last_player='O'):
        self.current_player = last_player
        self.player_1 = 'O'
        self.player_2 = 'X'
        self.board = [
            ['O','X','O'],
            ['X','O','X'],
            ['O','X','X']
        ]
    
    def print_board(self):
        """
            Returns board as a string
            e.g
            x | o | x
            o | x | o
            o | x | o
        """
        board = ""
        for i in range(3):
            for j in range(3):
                board += self.board[i][j]
                if j != 2:
                    board += " | "
            board += "\n"
        return board

    ########################### Player Functions ###########################
    def shift_player(self):
        if self.current_player == self.player_1:
            self.current_player = self.player_2
        else:
            self.current_player = self.player_1

    def get_current_player(self):
        """
            returns current player
        """
        return self.current_player
    ########################### Player Functions End ###########################

    ########################### Game Dynamics ###########################
    def win_game(self):
        pass
    
    def row_win(self):
        """
            returns true if current player has three in row 
        """
        win = True
        for i in range(len(self.board)):
            win = True
            for j in range( len(self.board) ):
                if self.board[i][j] != self.current_player:
                    win = False
                    break
            if win:
                return win
        return win

    def col_win(self):
        """
            returns true if current player has three in column 
        """
        win = True
        for i in range( len(self.board) ):
            win = True
            for j in range( len(self.board) ):
                if self.board[j][i] != self.current_player:
                    win = False
                    break
            if win:
                return win
        return win

    def diag_win(self):
        win = True
        board_len = len(self.board)
        for i in range(len(self.board)):
            win = True
            for j in range(board_len):
                # For principal diagonal
                if (i==j or i+j == board_len-1) and self.board[i][j] != self.current_player:
                    win = False
                    break  
            if win:
                return win
        return win 
    ########################### Game Dynamics Ends ###########################

obj = TicTacToe()
print( obj.print_board())

a = obj.diag_win()
print(a)


# a = obj.row_win()
# print(a)
# obj.shift_player()
# a = obj.col_win()
# print(a)


# a = obj.get_current_player()
# print( a)
# obj.shift_player()

# a = obj.get_current_player()
# print( a)
# obj.shift_player()
