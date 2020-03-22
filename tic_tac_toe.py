import random
class TicTacToe():
    def __init__(self,player_1= 'O', player_2 = 'X', last_player='O'):
        self.current_player = last_player
        self.player_1 = player_1
        self.player_2 = player_2
        self.move_count = 0
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' ']
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
        for i in range(3):#need to change this in the future
            for j in range(3):#need to change this in the future
                board += self.board[i][j]
                if j != 2:#need to change this in the future
                    board += " | "
            board += "\n"
        return board

    def print_hint_board(self):
        """
            Returns board as a string
            e.g
            1 | 2 | 3
            4 | 5 | 6
            7 | 8 | 9 
        """
        board = ""
        count = 1 
        for i in range(3):#need to change this in the future
            for j in range(3):#need to change this in the future
                board += str(count) 
                count += 1
                if j != 2:#need to change this in the future
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
    
    def get_move(self, user_input): 
        #Need to change this code part in the future to make it dynamic
        is_valid = False
        i =0
        j=0
        if user_input == 1:
            is_valid = self.is_valid_move(0,0)
            i=0
            j=0
        elif user_input == 2:
            is_valid = self.is_valid_move(0,1)
            i=0
            j=1
        elif user_input == 3:
            is_valid = self.is_valid_move(0,2)
            i=0
            j=2
        elif user_input == 4:
            is_valid = self.is_valid_move(1,0)
            i=1
            j=0
        elif user_input == 5:
            is_valid = self.is_valid_move(1,1)
            i=1
            j=1
        elif user_input == 6:
            is_valid = self.is_valid_move(1,2)
            i=1
            j=2
        elif user_input == 7:
            is_valid = self.is_valid_move(2,0)
            i=2
            j=0
        elif user_input == 8:
            is_valid = self.is_valid_move(2,1)
            i=2
            j=1
        elif user_input == 9:
            is_valid = self.is_valid_move(2,2)
            i=2
            j=2

        if is_valid:
            self.make_move(i,j)
            self.move_count += 1
        return is_valid

    def is_valid_move(self,i,j):
        if self.board[i][j] == ' ':
            return True
        return False

    def make_move(self,i,j):
        self.board[i][j] = self.current_player

    def win_game(self):
        if self.row_win() or self.col_win() or self.diag_win():
            return True
        return False

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
        # Need to change this in future
        if self.board[0][0] == self.current_player and self.board[1][1] == self.current_player and self.board[2][2] == self.current_player or self.board[0][2] == self.current_player and self.board[1][1] == self.current_player and self.board[0][2] == self.current_player:
            return True
        return False

    def game_over(self):
        if self.move_count == 9 or self.win_game():
            return True
        return False
    ########################### Game Dynamics Ends ###########################
    

