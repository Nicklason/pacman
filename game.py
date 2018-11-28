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
            x = self.player.pos[0]
            y = self.player.pos[1]

            self.player.above = self.map.grid_type(
                [x, y-self.player.speed], True) is Map.WALL or self.map.grid_type([x+15, y-self.player.speed], True) is Map.WALL
            self.player.below = self.map.grid_type(
                [x, y+15+self.player.speed], True) is Map.WALL or self.map.grid_type([x+15, y+16], True) is 1
            self.player.right = self.map.grid_type(
                [x+15+self.player.speed, y], True) is Map.WALL or self.map.grid_type([x+15+self.player.speed, y+15], True) is Map.WALL
            self.player.left = self.map.grid_type(
                [x-self.player.speed, y], True) is Map.WALL or self.map.grid_type([x-self.player.speed, y+15], True) is Map.WALL

            self.player.tick(pressed)
    
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
