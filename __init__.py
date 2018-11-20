from game import Game
from viewer import Viewer

# Initialiser spil klasse
game = Game()
# Indlæs bane
game.load_map('maps/default.png')
# Initialiser viewer klasse
viewer = Viewer(game)

# Start spillet
game.start_game()
# Start loop
viewer.start_clock()
