import random
class TicTacToe():
    def __init__(self,player_1= 'O', player_2 = 'X', last_player='O'):
        self.current_player = last_player
        self.player_1 = player_1
        self.player_2 = player_2
        self.move_count = 0

        self.x = -1 # row of matrix
        self.y = -1 # column of matrix
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
        if user_input == 1:
            is_valid = self.is_valid_move(0,0)
            self.x = 0
            self.y = 0
        elif user_input == 2:
            is_valid = self.is_valid_move(0,1)
            self.x = 0
            self.y = 1
        elif user_input == 3:
            is_valid = self.is_valid_move(0,2)
            self.x = 0
            self.y = 2
        elif user_input == 4:
            is_valid = self.is_valid_move(1,0)
            self.x = 1
            self.y = 0
        elif user_input == 5:
            is_valid = self.is_valid_move(1,1)
            self.x = 1
            self.y = 1
        elif user_input == 6:
            is_valid = self.is_valid_move(1,2)
            self.x = 1
            self.y = 2
        elif user_input == 7:
            is_valid = self.is_valid_move(2,0)
            self.x = 2
            self.y = 0
        elif user_input == 8:
            is_valid = self.is_valid_move(2,1)
            self.x = 2
            self.y = 1
        elif user_input == 9:
            is_valid = self.is_valid_move(2,2)
            self.x = 2
            self.y = 2
        return is_valid

    def is_valid_move(self,i,j):
        if self.board[i][j] == ' ':
            return True
        return False

    def make_move(self):
        self.board[self.x][self.y] = self.current_player
        self.move_count += 1

    def game_draw(self):
        return self.move_count == 9 and not self.win_game()

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
        if self.game_draw() or self.win_game():
            return True
        return False
    ########################### Game Dynamics Ends ###########################
