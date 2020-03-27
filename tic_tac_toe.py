import random
class TicTacToe():
    def __init__(self,player_1= 'X', player_2 = 'O', last_player='X'):
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

    ########################### Player Functions End ###########################

    ########################### Game Dynamics ###########################
    
    def set_move(self, user_input): 
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

    def check_winner(self):
        winner = None
        board_length = len(self.board)
        
        # Horizontal Winner
        for i in range(board_length):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                winner = self.board[i][0]

        # Vertical Winner
        for i in range(board_length):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                winner = self.board[0][i]

        # Principle Diagonal Winner
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            winner = self.board[0][0]

        # Secondary Diagonal Winner
        if self.board[2][0] == self.board[1][1] == self.board[0][2] != ' ':
            winner = self.board[2][0]

        open_spots = 0

        for i in range(board_length):
            for j in range(board_length):
                if self.board[i][j] == ' ':
                    open_spots += 1

        if winner == None and open_spots == 0:
            return 'tie'
        else:
            return winner
    ########################### Game Dynamics Ends ###########################
    