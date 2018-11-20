""" Game klassen """

from gamemap import Map

class Game:
    """ Initialiserer game klasse """
    def __init__(self):
        self.state = 0

    def load_map(self, file_name):
        """ Indlæser bane """
        # Initialiserer map klasse
        self.map = Map(file_name)

    def tick(self, pressed):
        """ Kaldes hver iteration i spil loopet """
        pass

    def start_game(self):
        """ Starter spillet """
        if self.state == 0:
            self.state = 1

    def end_game(self):
        """ Stopper spillet """
        if self.state > 0:
            self.state = 0

    def toggle_pause(self):
        """ Pauser spillet """
        if self.state == 1:
            self.state = 2
        else:
            self.state = 1
