""" Game klassen """

from gamemap import Map
from player import Player

class Game:
    """ Initialiserer game klasse """
    def __init__(self):
        self.state = 0

    def load_map(self, file_name):
        """ Indlæser bane """
        # Initialiserer map klasse
        self.map = Map(file_name)

        # Find ud af hvor spilleren er
        player_pos = self.map.get_player_pos()
        if player_pos is not None:
            self.player = Player(player_pos)

    def tick(self, pressed):
        """ Kaldes hver iteration i spil loopet """

        if self.player:
            # self.moveability(player)
            # hvilke veje kan spilleren bevæge sig?
            self.player.tick(pressed)
        pass
    
    def moveability(self):
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
