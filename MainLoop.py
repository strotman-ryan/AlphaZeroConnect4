#Title: Main game of connect 4
#Synopsis: Make the main game loop for connect 4

from Game import Game
from HumanPlayer import HumanPlayer
from GameManager import GameManager
from RandomPlayer import RandomPlayer

player1 = RandomPlayer()
player2 = RandomPlayer()

game = Game(player1, player2,7,6)

manager = GameManager(game)
manager.RunGame()





    


