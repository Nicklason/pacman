""" Game klassen """

from gamemap import Map
from player import Player

class Game:
    """ Initialiserer game klasse """
    def __init__(self):
        self.state = 0
        self.score = 0

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

            self.player.above = self.map.grid_type([x, y-self.player.speed], True) is Map.WALL or self.map.grid_type([x+15, y-self.player.speed], True) is Map.WALL
            self.player.below = self.map.grid_type([x, y+15+self.player.speed], True) is Map.WALL or self.map.grid_type([x+15, y+16], True) is 1
            self.player.right = self.map.grid_type([x+15+self.player.speed, y], True) is Map.WALL or self.map.grid_type([x+15+self.player.speed, y+15], True) is Map.WALL
            self.player.left = self.map.grid_type([x-self.player.speed, y], True) is Map.WALL or self.map.grid_type([x-self.player.speed, y+15], True) is Map.WALL

            grid = self.map.get_grid(self.player.pos)

            if self.map.grid_type(grid) is None and self.map.inside_grid(self.player.pos) is True:
                # Teleporter spilleren til den modsatte side
                if self.player.direction in (2,3):
                    self.player.pos[0] = self.player.pos[0]%(self.map.width*16)
                else:
                    self.player.pos[1] = self.player.pos[0]%(self.map.height*16)
            elif self.map.grid_type(grid) is Map.POINT and self.map.inside_grid(self.player.pos) is True:
                # Hvis spilleren står inde i et grid med et point, og spilleren er helt inde i grid, så fjern
                # point fra banen og incrementer scoren 
                self.score += 10
                self.map.remove_point(grid)
                if self.map.removed_points == self.map.total_points:
                    # Der er ikke flere point i banen, start ny bane
                    self.load_map("default.png")
            else:
                self.player.tick(pressed)
    
    def start_game(self):
        """ Starter spillet """
        if self.state == 0:
            # Starter et nyt spil
            self.state = 1
        elif self.state == 3:
            # Spillet er stoppet, starter et nyt
            self.state = 1
            self.score = 0
            self.load_map("default.png")

    def end_game(self):
        """ Stopper spillet """
        self.state = 3

    def toggle_pause(self):
        """ Pauser spillet """
        if self.state == 1:
            # Spillet er i gang, pauser det
            self.state = 2
        elif self.state == 2:
            # Spillet er pauset, starter det
            self.state = 1
