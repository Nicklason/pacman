from game import Game
from viewer import Viewer

game = Game()
game.load_map('maps/default.png')
viewer = Viewer(game)

game.start_game()
viewer.start_clock()
