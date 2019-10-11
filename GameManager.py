#Game Manager



class GameManager:
    
    
    
    def __init__(self,game):
        self.game = game
        
    def RunGame(self):
        while(True):
            self.game.PrintBoard()
            self.game.Move()
            self.game.ChangePlayerTurn()