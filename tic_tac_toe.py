import random
class TicTacToe():
    def __init__(self,last_player='O'):
        self.current_player = last_player
        self.player_1 = 'O'
        self.player_2 = 'X'
        self.board = [
            ['','',''],
            ['','',''],
            ['','','']
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
            self.shift_player()
        return is_valid

        


    def is_valid_move(self,i,j):
        if self.board[i][j] == '':
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

count =0
while count < 9:
    a = input()
    b = obj.get_move(int(a))

    if not b:
        print("Cannot")
        continue
    print(obj.print_board())
    count += 1


# a = obj.win_game()
# print(a)


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
