#The game class
#an instance of this class controls one game

import numpy as np

class Game:
    
    '''
    Contructor to initilize the game
    column: int the number of columns
    rows: int the number of rows
    player1: the AI that will be player1
    player2 the AI that will be player2
    #TODO make an interface for players
    board: numpy array (row x column) (index starting at 0)
    - 1 is player 1
    - -1 is player 2
    - 0 if empty
    player_turn: true if player1; false if player2
    toWin: number in a row to win (normally 4)
    '''
    def __init__(self,player1,player2,columns = 7,rows = 6, toWin = 4):
        self.colums = columns
        self.rows = rows
        self.player1 = player1
        self.player2 = player2
        self.board = np.zeros((rows,columns))
        self.player_turn = True
        self.toWin = toWin
        
    #printboard
    def PrintBoard(self):
        print(self.board)
        
    #Update the board 
    #Assume the move is legal
    def addPlayerMove(self,column):
        row = np.max(np.where(self.board[:,column] == 0))
        self.board[row,column] = 1 if self.player_turn else -1
        
    #Switch the player variable from p1 -> p2 or vice versa
    def ChangePlayerTurn(self):
        self.player_turn = not self.player_turn
        
    def getMove(self):
        return self.player1.MakeMove(self.board) if self.player_turn else self.player2.MakeMove(self.board)
    
    def Move(self):
        column = self.getMove()
        self.addPlayerMove(column)
        
    #checks to see if board is filled
    #returns true if all spaces filled
    def IsBoardFilled(self):
        return self.rows * self.columns == np.count_nonzero(self.board)
    
    #returns true if <player> won
    def PlayerWin(self,player):
        pass
    
    
    
    



