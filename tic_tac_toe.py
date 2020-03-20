import random
class TicTacToe():
    def __init__(self,last_player=1):
        self.current_player = last_player
        self.player_1 = 1
        self.player_2 = 2
        self.board = [
            ['1','2','3'],
            ['4','5','6'],
            ['7','8','9']
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

    ########################### Game Dynamics Ends ###########################

obj = TicTacToe()
print( obj.print_board())


a = obj.get_current_player()
print( a)
obj.shift_player()

a = obj.get_current_player()
print( a)
obj.shift_player()
