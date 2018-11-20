""" Fil som starter programmet """

from game import Game
from viewer import Viewer

if __name__ == "__main__":
    # Initialiser spil klasse
    GAME = Game()
    # Indlæs bane
    GAME.load_map('maps/default.png')
    # Initialiser viewer klasse
    VIEWER = Viewer(GAME)

    # Start spillet
    GAME.start_game()
    # Start loop
    VIEWER.start_clock()
