""" Fil som starter programmet """

if __name__ == "__main__":
    from viewer import Viewer
    from game import Game

    # Initialiser spil klasse
    GAME = Game()
    # Indlæs bane
    GAME.load_map('default.png')
    # Initialiser viewer klasse
    VIEWER = Viewer(GAME)
    
    # Start loop
    VIEWER.start_clock()
