""" Fil som starter programmet """

if __name__ == "__main__":
    from viewer import Viewer
    from game import Game

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
