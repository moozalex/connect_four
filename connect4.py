#Alex Moozhayil

#-------------------------------------------------------------------------------
# Name:        connect4.py
# Purpose:     both an interactive and one-move A.I. program/game
#
#    
# Citations:       Some functions were provided by Dr. Vamsikrishna Gopikrishna.
#              Additionally, I have attached a github link by author Keith Galli
#              that informed me on how to address the connect four problem, different useful functions,
#              and provided his perspective on scoring. Link below:
#              https://github.com/KeithGalli/Connect4-Python
#              Pseudocode for minimax found on wikipedia: https://en.wikipedia.org/wiki/Minimax#Pseudocode
#
#              Pseudocode for pruning found on wikipedia: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning#Pseudocode
#               
#              I have created an OOP connect 4 game that includes minimax and pruning.
#-------------------------------------------------------------------------------

import sys
import math
import random
import copy
from time import process_time


# Function provided by Dr. Vamsikrishna Gopikrishna
class maxConnect4Game:
    def __init__(self, board, player1Score, player2Score):
        self.player1Score = player1Score
        self.player2Score = player2Score
        self.board = board

    # Calculate the number of 4-in-a-row each player has
    def get_score_one(self):
        return self.player1Score


    def get_score_two(self):
        return self.player2Score
    
    
    def countScore(self):
        self.player1Score = 0
        self.player2Score = 0


        # Check horizontally
        for row in self.board:
            # Check player 1
            if row[0:4] == [1]*4:
                self.player1Score += 1
            if row[1:5] == [1]*4:
                self.player1Score += 1
            if row[2:6] == [1]*4:
                self.player1Score += 1
            if row[3:7] == [1]*4:
                self.player1Score += 1
            # Check player 2
            if row[0:4] == [2]*4:
                self.player2Score += 1
            if row[1:5] == [2]*4:
                self.player2Score += 1
            if row[2:6] == [2]*4:
                self.player2Score += 1
            if row[3:7] == [2]*4:
                self.player2Score += 1


        # Check vertically
        for j in range(7):
            # Check player 1
            if (self.board[0][j] == 1 and self.board[1][j] == 1 and
                    self.board[2][j] == 1 and self.board[3][j] == 1):
                self.player1Score += 1
            if (self.board[1][j] == 1 and self.board[2][j] == 1 and
                    self.board[3][j] == 1 and self.board[4][j] == 1):
                self.player1Score += 1
            if (self.board[2][j] == 1 and self.board[3][j] == 1 and
                    self.board[4][j] == 1 and self.board[5][j] == 1):
                self.player1Score += 1
            # Check player 2
            if (self.board[0][j] == 2 and self.board[1][j] == 2 and
                    self.board[2][j] == 2 and self.board[3][j] == 2):
                self.player2Score += 1
            if (self.board[1][j] == 2 and self.board[2][j] == 2 and
                    self.board[3][j] == 2 and self.board[4][j] == 2):
                self.player2Score += 1
            if (self.board[2][j] == 2 and self.board[3][j] == 2 and
                    self.board[4][j] == 2 and self.board[5][j] == 2):
                self.player2Score += 1

        # Check diagonally

        # Check player 1
        if (self.board[2][0] == 1 and self.board[3][1] == 1 and
                self.board[4][2] == 1 and self.board[5][3] == 1):
            self.player1Score += 1
        if (self.board[1][0] == 1 and self.board[2][1] == 1 and
                self.board[3][2] == 1 and self.board[4][3] == 1):
            self.player1Score += 1
        if (self.board[2][1] == 1 and self.board[3][2] == 1 and
                self.board[4][3] == 1 and self.board[5][4] == 1):
            self.player1Score += 1
        if (self.board[0][0] == 1 and self.board[1][1] == 1 and
                self.board[2][2] == 1 and self.board[3][3] == 1):
            self.player1Score += 1
        if (self.board[1][1] == 1 and self.board[2][2] == 1 and
                self.board[3][3] == 1 and self.board[4][4] == 1):
            self.player1Score += 1
        if (self.board[2][2] == 1 and self.board[3][3] == 1 and
                self.board[4][4] == 1 and self.board[5][5] == 1):
            self.player1Score += 1
        if (self.board[0][1] == 1 and self.board[1][2] == 1 and
                self.board[2][3] == 1 and self.board[3][4] == 1):
            self.player1Score += 1
        if (self.board[1][2] == 1 and self.board[2][3] == 1 and
                self.board[3][4] == 1 and self.board[4][5] == 1):
            self.player1Score += 1
        if (self.board[2][3] == 1 and self.board[3][4] == 1 and
                self.board[4][5] == 1 and self.board[5][6] == 1):
            self.player1Score += 1
        if (self.board[0][2] == 1 and self.board[1][3] == 1 and
                self.board[2][4] == 1 and self.board[3][5] == 1):
            self.player1Score += 1
        if (self.board[1][3] == 1 and self.board[2][4] == 1 and
                self.board[3][5] == 1 and self.board[4][6] == 1):
            self.player1Score += 1
        if (self.board[0][3] == 1 and self.board[1][4] == 1 and
                self.board[2][5] == 1 and self.board[3][6] == 1):
            self.player1Score += 1


        if (self.board[0][3] == 1 and self.board[1][2] == 1 and
                self.board[2][1] == 1 and self.board[3][0] == 1):
            self.player1Score += 1
        if (self.board[0][4] == 1 and self.board[1][3] == 1 and
                self.board[2][2] == 1 and self.board[3][1] == 1):
            self.player1Score += 1
        if (self.board[1][3] == 1 and self.board[2][2] == 1 and
                self.board[3][1] == 1 and self.board[4][0] == 1):
            self.player1Score += 1
        if (self.board[0][5] == 1 and self.board[1][4] == 1 and
                self.board[2][3] == 1 and self.board[3][2] == 1):
            self.player1Score += 1
        if (self.board[1][4] == 1 and self.board[2][3] == 1 and
                self.board[3][2] == 1 and self.board[4][1] == 1):
            self.player1Score += 1
        if (self.board[2][3] == 1 and self.board[3][2] == 1 and
                self.board[4][1] == 1 and self.board[5][0] == 1):
            self.player1Score += 1
        if (self.board[0][6] == 1 and self.board[1][5] == 1 and
                self.board[2][4] == 1 and self.board[3][3] == 1):
            self.player1Score += 1
        if (self.board[1][5] == 1 and self.board[2][4] == 1 and
                self.board[3][3] == 1 and self.board[4][2] == 1):
            self.player1Score += 1
        if (self.board[2][4] == 1 and self.board[3][3] == 1 and
                self.board[4][2] == 1 and self.board[5][1] == 1):
            self.player1Score += 1
        if (self.board[1][6] == 1 and self.board[2][5] == 1 and
                self.board[3][4] == 1 and self.board[4][3] == 1):
            self.player1Score += 1
        if (self.board[2][5] == 1 and self.board[3][4] == 1 and
                self.board[4][3] == 1 and self.board[5][2] == 1):
            self.player1Score += 1
        if (self.board[2][6] == 1 and self.board[3][5] == 1 and
                self.board[4][4] == 1 and self.board[5][3] == 1):
            self.player1Score += 1


        # Check player 2
        if (self.board[2][0] == 2 and self.board[3][1] == 2 and
                self.board[4][2] == 2 and self.board[5][3] == 2):
            self.player2Score += 1
        if (self.board[1][0] == 2 and self.board[2][1] == 2 and
                self.board[3][2] == 2 and self.board[4][3] == 2):
            self.player2Score += 1
        if (self.board[2][1] == 2 and self.board[3][2] == 2 and
                self.board[4][3] == 2 and self.board[5][4] == 2):
            self.player2Score += 1
        if (self.board[0][0] == 2 and self.board[1][1] == 2 and
                self.board[2][2] == 2 and self.board[3][3] == 2):
            self.player2Score += 1
        if (self.board[1][1] == 2 and self.board[2][2] == 2 and
                self.board[3][3] == 2 and self.board[4][4] == 2):
            self.player2Score += 1
        if (self.board[2][2] == 2 and self.board[3][3] == 2 and
                self.board[4][4] == 2 and self.board[5][5] == 2):
            self.player2Score += 1
        if (self.board[0][1] == 2 and self.board[1][2] == 2 and
                self.board[2][3] == 2 and self.board[3][4] == 2):
            self.player2Score += 1
        if (self.board[1][2] == 2 and self.board[2][3] == 2 and
                self.board[3][4] == 2 and self.board[4][5] == 2):
            self.player2Score += 1
        if (self.board[2][3] == 2 and self.board[3][4] == 2 and
                self.board[4][5] == 2 and self.board[5][6] == 2):
            self.player2Score += 1
        if (self.board[0][2] == 2 and self.board[1][3] == 2 and
                self.board[2][4] == 2 and self.board[3][5] == 2):
            self.player2Score += 1
        if (self.board[1][3] == 2 and self.board[2][4] == 2 and
                self.board[3][5] == 2 and self.board[4][6] == 2):
            self.player2Score += 1
        if (self.board[0][3] == 2 and self.board[1][4] == 2 and
                self.board[2][5] == 2 and self.board[3][6] == 2):
            self.player2Score += 1

        if (self.board[0][3] == 2 and self.board[1][2] == 2 and
                self.board[2][1] == 2 and self.board[3][0] == 2):
            self.player2Score += 1
        if (self.board[0][4] == 2 and self.board[1][3] == 2 and
                self.board[2][2] == 2 and self.board[3][1] == 2):
            self.player2Score += 1
        if (self.board[1][3] == 2 and self.board[2][2] == 2 and
                self.board[3][1] == 2 and self.board[4][0] == 2):
            self.player2Score += 1
        if (self.board[0][5] == 2 and self.board[1][4] == 2 and
                self.board[2][3] == 2 and self.board[3][2] == 2):
            self.player2Score += 1
        if (self.board[1][4] == 2 and self.board[2][3] == 2 and
                self.board[3][2] == 2 and self.board[4][1] == 2):
            self.player2Score += 1
        if (self.board[2][3] == 2 and self.board[3][2] == 2 and
                self.board[4][1] == 2 and self.board[5][0] == 2):
            self.player2Score += 1
        if (self.board[0][6] == 2 and self.board[1][5] == 2 and
                self.board[2][4] == 2 and self.board[3][3] == 2):
            self.player2Score += 1
        if (self.board[1][5] == 2 and self.board[2][4] == 2 and
                self.board[3][3] == 2 and self.board[4][2] == 2):
            self.player2Score += 1
        if (self.board[2][4] == 2 and self.board[3][3] == 2 and
                self.board[4][2] == 2 and self.board[5][1] == 2):
            self.player2Score += 1
        if (self.board[1][6] == 2 and self.board[2][5] == 2 and
                self.board[3][4] == 2 and self.board[4][3] == 2):
            self.player2Score += 1
        if (self.board[2][5] == 2 and self.board[3][4] == 2 and
                self.board[4][3] == 2 and self.board[5][2] == 2):
            self.player2Score += 1
        if (self.board[2][6] == 2 and self.board[3][5] == 2 and
                self.board[4][4] == 2 and self.board[5][3] == 2):
            self.player2Score += 1


        


class Game:
    """This creates a Connect 4 Game"""   
    def __init__(self, row_count, col_count):
        """Initialize row count and column count"""
        self.row_count = row_count
        self.col_count = col_count
        self.board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
            ]

        self.player = 1
        self.AI = 2
        self.score_one = 0
        self.score_two = 0 

    def get_score_one(self):
        return self.score_one

    def get_score_two(self):
        return self.score_two

    def get_board(self):
        return self.board
    
    # Keith - this is fine
    def print_board(self):
        """Print the board values"""
        for row in reversed(range(self.row_count)):
            print(self.board[row])
    # Keith - this is fine
    def open_row(self, col):
        """show which row is available next"""
        for row in range(self.row_count):
            if self.board[row][col] == 0:
                return row

    # Keith -this is fine
    def valid_location(self, col):
        """Check if desired location is available"""
        return self.board[self.row_count-1][col] == 0
    
    # Keith - this is fine

    def play_piece_player(self, col, piece, player1Score, player2Score):
        """Drop a piece in desired location"""
        row = self.open_row(col)
        valid = self.valid_location(col)      
        if valid:
            self.board[row][col] = piece
        else:
            print("Column is full")

    def play_piece(self, board, col, piece, player1Score, player2Score):
        """Drop a piece in desired location"""
        row = self.open_row(col)
        valid = self.valid_location(col)      
        if valid:
            board[row][col] = piece
            score_keeper = maxConnect4Game(self.board, player1Score, player2Score)
            score_keeper.countScore()
            self.score_one = score_keeper.get_score_one()
            self.score_two = score_keeper.get_score_two()
        else:
            print("Column is full")


    
    def get_valid_locations(self):
        locations = []
        for col in range(self.col_count):
            if self.valid_location(col):
                locations.append(col)
        return locations

    def winning_move(self,piece):
        #check horizontal locations for win
        for col in range(self.col_count-3):
            for row in range(self.row_count):
                if self.board[row][col] == piece and self.board[row][col+1] == piece and self.board[row][col+2] == piece and self.board[row][col+3] == piece:
                    return True

        #check vertical locations for win
        for col in range(self.col_count):
            for row in range(self.row_count-3):
                if self.board[row][col] == piece and self.board[row+1][col] == piece and self.board[row+2][col] == piece and self.board[row+3][col] == piece:
                    return True

        #positive slope
        for col in range(self.col_count-3):
            for row in range(self.row_count-3):
                if self.board[row][col] == piece and self.board[row+1][col+1] == piece and self.board[row+2][col+2] == piece and self.board[row+3][col+3] == piece:
                    return True

        #negative slope
        for col in range(self.col_count-3):
            for row in range(3, self.row_count-3):
                if self.board[row][col] == piece and self.board[row-1][col+1] == piece and self.board[row-2][col+2] == piece and self.board[row-3][col+3] == piece:
                    return True

    def print_board_file(self, filename):
        """Print the board values"""
        for row in reversed(range(self.row_count)):
            print(self.board[row], file=open(filename, "a"))

            
    def terminal(self):
        return self.winning_move(self.AI) or self.winning_move(self.player) or len(self.get_valid_locations()) == 0

    
    
    def score_position(self, piece): 
        score = 0

        center_col = []
        row_array = []
        col_array = []
        range_col = self.col_count - 3
        range_row = self.row_count - 3

        for i in list(self.board[:][3]):
            center_col.append(i)
        center_col_counter = center_col.count(piece)
        score += center_col_counter * 6 
        

        #score for horizontal 
        for r in range(range_row):
            for i in self.board[r][:]:
                row_array.append(i)
                for c in range(range_col):
                    four_pieces = row_array[c:c+4]
                    if four_pieces.count(piece) == 4:
                        score += 100
                    elif four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score += 100*0.7
                    elif four_pieces.count(piece) == 2 and four_pieces.count(0) == 2:
                        score += 100*0.5
                    if four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score -= 100*0.3
        #vertical 
        for c in range(range_col):
            for i in list(self.board[:][c]):
                col_array.append(i)
                four_pieces = row_array[r:r+4]
                for r in range(range_row):
                    four_pieces = row_array[c:c+4]
                    if four_pieces.count(piece) == 4:
                        score += 100
                    elif four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score += 100*0.7
                    elif four_pieces.count(piece) == 2 and four_pieces.count(0) == 2:
                        score += 100*0.5
                    if four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score -= 100*0.3
        # positive slope
        for r in range(range_row):
            for c in range(range_col):
                for i in range(4):
                    four_pieces.append(self.board[r+i][c+i]) 
                    if four_pieces.count(piece) == 4:
                        score += 100
                    elif four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score += 100*0.7
                    elif four_pieces.count(piece) == 2 and four_pieces.count(0) == 2:
                        score += 100*0.5
                    if four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score -= 100*0.3
        #negative slope
        for r in range(range_row):
            for c in range(range_col):
                for i in range(range_col):
                    four_pieces.append(self.board[r+3-i][c+i]) 
                    if four_pieces.count(piece) == 4:
                        score += 100
                    elif four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score += 100*0.7
                    elif four_pieces.count(piece) == 2 and four_pieces.count(0) == 2:
                        score += 100*0.5
                    if four_pieces.count(piece) == 3 and four_pieces.count(0) == 1:
                        score -= 100*0.3
        return score 



    def minimax(self, board, depth, alpha, beta, maximizingPlayer, player1Score, player2Score, internalState = False):
        valid_locations = self.get_valid_locations()
        is_terminal = self.terminal()

        if internalState and (depth == 0 or is_terminal):
            if is_terminal:
                if self.winning_move(self.AI):
                    return (None, 1000000000000000000)
                elif self.winning_move(self.player):
                    return (None, -1000000000000000000)
                else:
                    return (None, 0)
            else:
                return (None, self.score_position(self.AI))

        if maximizingPlayer:
            start_value = -math.inf
            column = random.choice(valid_locations)
            for col in valid_locations:
                row = self.open_row(col)
                b_copy = copy.deepcopy(board)
                self.play_piece(b_copy, col, self.AI, player1Score, player2Score)
                minimax_return = self.minimax(board, depth-1, alpha, beta, False, player1Score, player2Score, True)[1]
                if minimax_return > start_value:
                    start_value = minimax_return
                    column = col
                alpha = max(alpha, start_value)
                if alpha >= beta:
                    break
            return column, start_value
        else:
            start_value = math.inf
            column = random.choice(valid_locations)

            for col in valid_locations:
                row = self.open_row(col)
                b_copy = copy.deepcopy(board)
                self.play_piece(b_copy, col, self.player, player1Score, player2Score)
                minimax_return = self.minimax(board, depth-1, alpha, beta, True, player1Score, player2Score, True)[1]
                if minimax_return < start_value:
                    start_value = minimax_return
                    column = col
                beta = min(beta, start_value)
                if alpha >= beta:
                    break
            return column, start_value 



def oneMoveGame2():

    
    # if not get_next_open_row:
    #     print("Board is full")
    #     sys.exit(0)

    player1Score = 0
    player2Score = 0
    board = Game(6, 7)
    game_mode = True
    turn = 0
    player = 1
    AI = 2

    board = Game(6, 7)
    game_mode = sys.argv[1]
    inFile = sys.argv[2]
    outFile = sys.argv[3]
    depth = sys.argv[4]
    
    try:
        gameFile = open(inFile, "r")
    except:
        sys.exit("Error opening file.")

    file_lines = gameFile.readlines()
    board.board = [[int(char) for char in line[0:7]] for line in reversed(file_lines[0:-1])]
    turn = int(file_lines[-1][0])
    gameFile.close()
    
    

    while game_mode:
        if turn == 1:
            board.print_board()
            print("\n")
            col = int(input("Player 1 enter the column of choice: ")) - 1
            if board.valid_location(col):
                board.play_piece_player(col, player, player1Score, player2Score)
                print("\n")
                board.print_board()
                print("Score player 1: " + str(board.get_score_one()))
                print("Score AI: " + str(board.get_score_two()))
                board.print_board_file(outFile)
                break
                #turn = 1
        else:
            col, value = board.minimax(board.get_board(), 6, -math.inf, math.inf, True, player1Score, player2Score)

            if board.valid_location(col):
                board.play_piece(board.get_board(), col, AI, player1Score, player2Score)
                board.print_board()
                print("Score player 1: " + str(board.get_score_one()))
                print("Score AI: " + str(board.get_score_two()))
                board.print_board_file(outFile)
                break 
                #turn = 0
def interactiveGame():


    player1Score = 0
    player2Score = 0
    board = Game(6, 7)
    game_mode = True
    turn = 0
    player = 1
    AI = 2

    while game_mode:
        if turn == 0:
            col = int(input("Player 1 enter the column of choice: ")) - 1
            if board.valid_location(col):
                board.play_piece_player(col, player, player1Score, player2Score)
                board.print_board()
                print(board.get_score_one())
                print(board.get_score_two())

                turn = 1
        else:
            #col = int(input("Player 2 enter the column of choice: ")) - 1
            col, value = board.minimax(board.get_board(), 6, -math.inf, math.inf, True, player1Score, player2Score)

            if board.valid_location(col):
                board.play_piece(board.get_board(), col, AI, player1Score, player2Score)
                board.print_board()
                print(board.get_score_one())
                print(board.get_score_two())
                turn = 0


if __name__ == "__main__":

    if len(sys.argv) < 4:
        print("You are now in interactive mode! Good luck!")
        interactiveGame()
    else:
        start = process_time()
        oneMoveGame2()
        stop = process_time()
        print("Elapsed: ", (stop-start))
